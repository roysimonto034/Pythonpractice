'''Thread Synchronization'''
import threading
import time
semaphore=threading.Semaphore=2   # can be accessed by 2 threads at a time

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

'''Working with Thread semaphore'''

def worker():
    with semaphore:
        print(f"{threading.current_thread().name} has started working")
        time.sleep(2)
        print(f"{threading.current_thread().is_alive}")
        print(f"{threading.current_thread().name} has finished working")

threads=[]

for i in range(5):
    t=threading.Thread(target=worker,name=f"Thread - {i+1}")
    threads.append(t)
    print(f"{t.name} has been created ")
    t.start()

for ip in threads:
    ip.join()
    print(f"{ip.name} has terminated")

print("All threads are finished")

#o/p

'''
    Thread - 1 has been created 
    Thread - 1 has started working
    Thread - 2 has been created 
    Thread - 2 has started working
    Thread - 3 has been created 
    Thread - 4 has been created 
    Thread - 5 has been created 
    <bound method Thread.is_alive of <Thread(Thread - 2, started 13540)>>
    Thread - 2 has finished working
    <bound method Thread.is_alive of <Thread(Thread - 1, started 12476)>>
    Thread - 1 has finished working
    Thread - 1 has terminated
    Thread - 2 has terminated
    Thread - 3 has started working
    Thread - 4 has started working
    <bound method Thread.is_alive of <Thread(Thread - 3, started 26044)>>
    Thread - 3 has finished working
    Thread - 3 has terminated
    <bound method Thread.is_alive of <Thread(Thread - 4, started 13992)>>
    Thread - 4 has finished working
    Thread - 5 has started working
    Thread - 4 has terminated
    <bound method Thread.is_alive of <Thread(Thread - 5, started 29432)>>
    Thread - 5 has finished working
    Thread - 5 has terminated
    All threads are finished

'''