# INTRODUCTION:

# This is a demo code for getting temperature readings 
# from the temperature sensor from a SenseHat connected to RPi3.

# However, this code can be modified as necessary.

# Note that I have added CHANGETHIS as a label so that you can search 
# for the code block or variable that needs to be changed.

# All you have to worry about is this: Modify the User Defined Method
# In the User Defined Method, return a float value of the data.

# Modify the Connected Device Name, Metrics Name and sampling function
# 
#

from liota.entities.entity import Entity
from liota.core.package_manager import LiotaPackage
from random import randint
import time
import socket
import logging
import random

log = logging.getLogger(__name__)

dependencies = ["iotcc_mqtt"]

# --------------------User Configurable Retry and Delay Settings------------------------------#

# The value mentioned below is the total number of Edge System being deployed in the infrastructure
# minimum 1 for 1K, 2 for 2K, 3 for 3K, 4 for 4K and  5 for 5K Edge Systems
no_of_edge_system_in_thousands = 1
# Number of Retries for Connection and Registrations
no_of_retries_for_connection = 5
# Retry delay Min Value in seconds
delay_retries_min = 600
# Retry delay Max Value in seconds
delay_retries_max = 1800

# Lambda Function Multiplier uses the above settings for calculating retry and delay logic
lfm = lambda x: x * no_of_edge_system_in_thousands
retry_attempts = lfm(no_of_retries_for_connection)
delay_retries = random.randint(lfm(delay_retries_min), lfm(delay_retries_max))


# ---------------------------------------------------------------------------
# This is a sample app to send Temperature Data from SenseHat to
# IoTCC using MQTT protocol as DCC Comms

# ---------------------------------------------------------------------------
# CHANGETHIS
# USER DEFINED METHOD:
# Between UDM Start and UDM End create as many functions as you want.
# Here, I have added the read_temperature function that will pull temperature
# data from SenseHat's temp sensor. 
# Please add the whole code (including libraries) under the function.
# The Return Value should be a float/int value. 
# Do type conversion if necessary.
#
# ===================
# UDM Start ++

def read_temperature():
    from sense_hat import SenseHat
    sense = SenseHat()
    return round(sense.get_temperature(), 2)

# UDM End --
#====================

# Base Class
# Two functions: Run and Cleanup.
# RUN: The function that runs on load - liotapkg load
# CLEANUP: The function that runs on unload - liotapkg unload
class PackageClass(LiotaPackage):
    def run(self, registry):

#        The execution function of a liota package.
#        Acquires "iotcc_mqtt" and "iotcc_mqtt_edge_system" from registry then register five devices
#        and publishes device metrics to the DCC
#        :param registry: the instance of ResourceRegistryPerPackage of the package
#        :return:


        from liota.entities.devices.simulated_device import SimulatedDevice
        from liota.entities.metrics.metric import Metric
        import copy

        # Acquire resources from registry
        self.iotcc = registry.get("iotcc_mqtt")
        # Creating a copy of edge_system object to keep original object "clean"
        self.iotcc_edge_system = copy.copy(registry.get("iotcc_mqtt_edge_system"))

        self.reg_devices = []
        self.metrics = []
        num_devices = 1

        try:
            # CHANGETHIS
            # Register device:
            # Here, you are registering a new device (Data Source)
            # Change the values in the quotes below in SimulatedDevice
            device = SimulatedDevice("Temperature001", "TemperatureSensor")
            log.info("Registration Started for Device {0}".format(device.name))
            # Device Registration attempts
            reg_attempts = 0
            # Started Device Registration attempts
            while reg_attempts <= retry_attempts:
                try:
                    reg_device = self.iotcc.register(device)
                    break
                except Exception as e:
                    if reg_attempts == retry_attempts:
                        raise
                    reg_attempts += 1
                    log.error(
                        'Trying Device {0} Registration failed with following error - {1}'.format(device.name, str(e)))
                    log.info('{0} Device Registration: Attempt: {1}'.format(device.name, str(reg_attempts)))
                    time.sleep(delay_retries)

            self.reg_devices.append(reg_device)
            # Attempts to set device relationship with edge system
            relationship_attempts = 0
            while relationship_attempts <= retry_attempts:
                try:
                    self.iotcc.create_relationship(self.iotcc_edge_system, reg_device)
                    break
                except Exception as e:
                    if relationship_attempts == retry_attempts:
                        raise
                    relationship_attempts += 1
                    log.error(
                        'Trying Device {0} relationship with Edge System failed with following error - {1}'.format(
                            device.name, str(e)))
                    log.info('{0} Device Relationship: Attempt: {1}'.format(device.name, str(relationship_attempts)))
                    time.sleep(delay_retries)
            # CHANGETHIS
            # Use the device name as identifier in the registry to easily refer the device in other packages
            # Modify the device_registry_name based on your need. 
            device_registry_name = "Temperature_001"
            registry.register(device_registry_name, reg_device)

            # Setting multiple properties by passing Dictonary object for Devices with the retry attempts
            # in case of exceptions
            prop_attempts = 0
            while prop_attempts <= retry_attempts:
                try:
                    # CHANGETHIS
                    # PROPERTIES OF THE DEVICE:
                    # Enter Key-Value pairs based on your need.
                    # It could be any Key and any Value as long as it is a string.
                    self.iotcc.set_properties(reg_device, {"Country": "USA", "State": "Georgia", "City": "Atlanta",
                                                           "Location": "AirWatch HQ", "Building": "Perimeter",
                                                           "Floor": "Fifth Floor"})
                    break
                except Exception as e:
                    prop_attempts = prop_attempts + 1
                    log.error('Exception while setting property for Device {0} - {1}'.format((device.name, str(e))))
                    log.info('Trying setting properties for Device {0}: Attempt - {1}'.format(device.name,
                                                                                              str(prop_attempts)))
                    time.sleep(delay_retries)

            try:
                # CHANGETHIS
                # Registering Metric for Device:
                # Modify metric_name, and sampling function, interval and aggregation_size
                # in metric_simulated_received.
                # Copy and paste the try section to add more metrics.
                # REG_METRIC ++
                metric_name = "Temperature_C"
                metric_simulated_received = Metric(name=metric_name, unit=None, interval=5, aggregation_size=1,
                                                   sampling_function=read_temperature)
                reg_metric_simulated_received = self.iotcc.register(metric_simulated_received)
                self.iotcc.create_relationship(reg_device, reg_metric_simulated_received)
                reg_metric_simulated_received.start_collecting()
                self.metrics.append(reg_metric_simulated_received)
            except Exception as e:
                log.error(
                    'Exception while loading metric {0} for device {1} - {2}'.format(metric_name, device.name, str(e)))

        except Exception:
            log.info("Device Registration and Metrics loading failed")
            raise

    def clean_up(self):
        """
        The clean up function of a liota package.
        Unregister Device and Stops metric collection
        :return:
        """
        # On the unload of the package the device will get unregistered and the entire history will be deleted
        # from Pulse IoT Control Center so comment the below logic if the unregsitration of the device is not required
        # to be done on the package unload
        for metric in self.metrics:
            metric.stop_collecting()
        for device in self.reg_devices:
            self.iotcc.unregister(device)
        log.info("Cleanup completed successfully")