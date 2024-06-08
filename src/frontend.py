import time

def print_dots(stop_event):
    while not stop_event.is_set():
        print(".", end="", flush=True)
        time.sleep(0.5)
