import threading
import time


def worker(name):
    print(f"Worker {name} starting")
    time.sleep(2)
    print(f"Worker {name} finished")


threads = []

for i in range(5):
    # Creates a new thread that will execute the worker function with the current loop index i as an argument.
    # args(i,) is used to pass arguments to target function, and we need the trailing comma args parameter expects a tuple.
    # If we do -> args(i), it would be  interpreted as a function call with i as an argument, which is not what we want.
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)

    # Starts the thread, causing it to run the worker function
    t.start()

"""
The main thread is the initial thread of execution that starts when a Python program begins.
It is the thread in which the main part of your program runs.
When you create new threads, they run concurrently with the main thread.

The join() method is used to ensure that the main thread waits for all the worker threads to complete
their tasks before it finishes its own execution.
Without the join() calls, the main thread could finish and exit the program
while the worker threads are still running. By using join(),
you ensure that the main thread remains active until all the worker threads have completed their execution.
"""
for t in threads:
    # The join() method blocks the main thread until the thread t has completed its execution.
    t.join()

print("All workers finished!")
