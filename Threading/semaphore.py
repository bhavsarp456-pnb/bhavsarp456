#semaphore
from threading import Thread, Semaphore
from time import sleep
sem = Semaphore()
def fun1():
    print("Function Started")
    sem.acquire()
    for x in range(1,5):
        print(f"Fucntion1 Working - {x}")
        sleep(1)
    sem.release()
    print("Function1 Finished")

def fun2():
    print("Function2 Starting")
    while not sem.acquire(blocking=False):
        print("Function2: Semaphore is not available")
        sleep(1)
    else:
        print("Got Semaphore")
        for x in range(1,5):
            print(f"Function2 Working - {x}")
            sleep(1)
    print("Function2 Finished")
    sem.release()

t1 = Thread(target=fun1)
t2 = Thread(target=fun2)
t1.start()
t2.start()
t1.join()
t2.join()

print("All threads are done! exiting!")