import threading
import time

semaphore = threading.BoundedSemaphore(2)


def task():
    print("Trying to acquire semaphore...")
    semaphore.acquire()
    print("Semaphore acquired.")
    time.sleep(1)
    semaphore.release()
    print("Semaphore released.")


# Start threads
threads = [threading.Thread(target=task) for _ in range(4)]

for t in threads:
    t.start()
for t in threads:
    t.join()
