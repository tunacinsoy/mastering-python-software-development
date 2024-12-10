import threading
import time

# Shared resource
balance = 0
rlock = threading.RLock()


def deposit(amount: int) -> None:
    global balance
    with rlock:  # Acquire RLock
        balance += amount
        log_transaction("Deposit", amount)


# If we used a regular Lock, the function below would result in a deadlock
# because log_transaction would attempt to reacquire a lock that’s already held by the same thread.


def log_transaction(transaction_type: str, amount: int) -> None:
    with rlock:  # Reacquire RLock
        print(f"{transaction_type} of {amount} completed. Balance: {balance}")


# Create threads
threads = [threading.Thread(target=deposit, args=(100,)) for _ in range(3)]

start_time = time.time()

for t in threads:
    t.start()

for t in threads:
    t.join()

end_time = time.time()

print("Execution Time:", end_time - start_time, "seconds")
