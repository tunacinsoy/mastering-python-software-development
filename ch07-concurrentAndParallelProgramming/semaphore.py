import threading
import time

# Semaphore with a maximum of 2 permits
"""
Semaphore in Python is a synchronization primitive from the threading module that limits access to a shared resource by maintaining a counter.
It allows a fixed number of threads to access the resource concurrently.
"""
semaphore = threading.Semaphore(2)


def access_resource(thread_id):
    print(f"Thread-{thread_id} attempting to acquire the semaphore.")
    # Using `with semaphore` ensures the semaphore is released automatically when the block is exited
    # even in case of exceptions.
    with semaphore:  # Acquire the semaphore
        print(f"Thread-{thread_id} acquired the semaphore.")
        time.sleep(4)  # Simulate work with the resource
        print(f"Thread-{thread_id} releasing the semaphore.")


# Create 5 threads
threads = [threading.Thread(target=access_resource, args=(i,)) for i in range(5)]

# Start threads
for t in threads:
    t.start()

# Wait for threads to complete
for t in threads:
    t.join()
