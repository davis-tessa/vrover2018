import threading

sharedList = []

def appender(theList):
    print("Updating the list")
    theList.push("hello")

worker = threading.Thread(group=None, target=appender, name="Whatever", kwargs={ "theList": sharedList })

worker.start
worker.join

print(sharedList)
