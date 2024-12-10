import threading
import time

# Shared resource
queue = []
"""
Condition is a synchronization primitive that allows threads to wait for certain conditions to be met before proceeding.
It is part of the threading module and is often used in scenarios where threads need to communicate or coordinate.
"""
condition = threading.Condition()


# Producer function
def producer():
    for i in range(5):
        time.sleep(1)  # To see the output clearly
        with condition:  # Acquire the lock
            queue.append(i)
            print(f"Produced: {i}")
            """
            When a producer thread produces an item and calls condition.notify(),
            it wakes up one of the waiting consumer threads.
            The notified consumer thread will then attempt to reacquire the lock.
            """
            # condition.notify()  # Notify only a single waiting thread
            condition.notify_all()  # would notify all waiting threads


# Consumer function
def consumer():
    for _ in range(5):
        with condition:  # Acquire the lock
            while not queue:  # Wait until the queue is not empty
                """
                When a consumer thread finds the queue empty, it calls condition.wait().
                This releases the lock and puts the consumer thread in a waiting state.
                The consumer thread will remain in this state until it is notified by a producer thread.
                """
                condition.wait()
            item = queue.pop()  # Consume an item
            print(f"Consumed: {item}")


# Create threads

"""
The operating system's thread scheduler manages the execution of threads.
Even though producer threads are defined before consumer threads,
the scheduler will switch between threads, giving each thread a chance to run.
"""
producer_thread = [threading.Thread(target=producer) for _ in range(3)]
consumer_thread = [threading.Thread(target=consumer) for _ in range(3)]


for t in producer_thread:
    t.start()

for t in consumer_thread:
    t.start()


for t in consumer_thread:
    t.join()


for t in producer_thread:
    t.join()
