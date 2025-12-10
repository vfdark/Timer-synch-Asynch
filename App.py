import threading
import time
import os

def clear_screen():
    os.system('clear')  # macOS/Linux

def number_timer():
    """
    Prints 3 numbers at a time every 2 seconds.
    Demonstrates burst output.
    """
    n = 1
    while True:
        clear_screen()  # clears screen to show new burst
        numbers = ""
        for _ in range(3):  # print 3 numbers
            numbers += str(n) + " "
            n += 1
        print(numbers)
        time.sleep(2)  # wait 2 seconds for next burst

def bar_timer():
    """
    Prints "|" every 0.5 seconds.
    Runs asynchronously with the number timer.
    """
    while True:
        print("|", end="", flush=True)
        time.sleep(0.5)

# Create threads
t1 = threading.Thread(target=number_timer)
t2 = threading.Thread(target=bar_timer)

# Start both timers asynchronously
t1.start()
t2.start()
