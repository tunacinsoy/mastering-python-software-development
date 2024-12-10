import threading
import time

# Event object
# The event object manages an internal flag that can be set to true or false.
event = threading.Event()


# Worker function
def worker(id: int):
    # Let's include this to see that there are blocked threads, waiting for the flag to be set to True
    time.sleep(3)
    print(
        f"The worker thread {id} will set the flag to true right now to unblock waiting threads..."
    )

    # Sets the flag to True. All waiting threads are unblocked.
    event.set()

    print(
        f"The worker thread {id} will set the flag to false right now to block waiting threads..."
    )
    # Resets the flag to False. Threads calling wait() will block again.
    event.clear()


def waiter(id: int):
    print(f"Waiter {id} waiting for the event to be set...")
    event.wait()  # Wait until the event is set
    print(f"Event is set! Waiter {id} starts processing...")
    time.sleep(2)  # Simulate work
    print(f"Waiter {id} finished processing.")


# Create and start threads
# worker_thread = threading.Thread(target=worker)
producer_thread = [threading.Thread(target=worker, args=(i,)) for i in range(0, 1)]
consumer_thread = [threading.Thread(target=waiter, args=(i,)) for i in range(0, 2)]


for t in producer_thread:
    t.start()

for t in consumer_thread:
    t.start()

for t in producer_thread:
    t.join()

for t in consumer_thread:
    t.join()
