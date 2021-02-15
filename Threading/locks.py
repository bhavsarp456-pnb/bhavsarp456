#locks
from threading import Thread as t1, Lock
l = Lock()
g = 0
def add_one():
    global g
    l.acquire()
    g += 1
    l.release()

def add_two():
    global g
    l.acquire()
    g += 2
    l.release()

threads = []

for func in [add_one,add_two]:
    threads.append(t1(target=func))
    threads[-1].start()

for eachthread in threads:
    eachthread.join()

print(g)