'''Thread Synchronization'''
import threading
import time

shared_resource = 0
lock = threading.Lock()


def increment_resource():
    global shared_resource
    with lock:  # Acquires the lock upon entering the block
        local_copy = shared_resource
        time.sleep(0.01) # Simulate some work
        shared_resource = local_copy + 1
    # Lock is automatically released upon exiting the 'with' block


threads = []
for _ in range(10):
    thread = threading.Thread(target=increment_resource)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print(f"Final shared resource value: {shared_resource}")


'''Thread Safe Singleton'''

import threading

class Singleton:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:  # Double-checked locking
                    cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

# Example usage
def test_singleton():
    s = Singleton()
    print(f"Instance ID: {id(s)}")

threads = []
for _ in range(5):
    t = threading.Thread(target=test_singleton)
    t.start()
    threads.append(t)

for t in threads:
    t.join()