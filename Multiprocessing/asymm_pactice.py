from multiprocessing import Process
from os import getpid
def worker1():
    print(f"Process ID for worker 1 : {getpid()}")

def worker2():
    print(f"Process ID for worker 2 : {getpid()}")

if __name__ == "__main__":
    p1 = Process(target = worker1)
    p2 = Process(target = worker2)

    print(f"Process ID pf main Process : {getpid()}")

    p1.start()
    p2.start()

    print(f"Process ID of p1 using multiprocessing: {p1.pid}")
    print(f"Process ID of p2 using multiprocessing: {p2.pid}")

    p1.join()
    p2.join()

    print(f"Process p1 is alive : {p1.is_alive()}")
    print(f"Process p2 is alive : {p2.is_alive()}")

    