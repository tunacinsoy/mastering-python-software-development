import threading
import time

# Shared resource
counter = 0

# A mutex (mutual exclusion) lock is created to ensure that
# only one thread can access the critical section of the code at a time.
mutex = threading.Lock()


def increment():
    global counter
    for _ in range(1000000):
        # with keyword ensures that the lock is acquired before entering the critical section
        # and released after exiting it, preventing race conditions.
        with mutex:  # Acquire the lock
            counter += 1  # Critical section


threads = [threading.Thread(target=increment) for _ in range(2)]

start_time = time.time()

for t in threads:
    t.start()

for t in threads:
    t.join()

end_time = time.time()

print("Counter:", counter)  # Expected output: 2000000
print("Execution Time:", end_time - start_time, "seconds")

# With mutex, the elapsed time is 4 times more, since threads wait each other to do the function
