import time

def printDots(stopEvent):
    while not stopEvent.is_set():
        print(".", end="", flush=True)
        time.sleep(0.5)
