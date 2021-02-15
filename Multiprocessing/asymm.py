import multiprocessing
import os

def worker1():
    print(f"Process ID for worker 1: {os.getpid()}")

def worker2():
    print(f"Process ID for worker 2: {os.getpid()}")

if __name__ == "__main__":
    p1 = multiprocessing.Process(target = worker1)
    p2 = multiprocessing.Process(target = worker2)

    print(f"Process ID of Main Process: {os.getpid()}")

    p1.start()
    p2.start()

    print(f"Process ID of p1 using multiprocessing: {p1.pid}")
    print(f"Process ID of p2 using multiprocessing: {p2.pid}")
    p1.join()
    p2.join()

    print(f"Process p1 is alive: {p1.is_alive()}")
    print(f"Process p2 is alive: {p2.is_alive()}")