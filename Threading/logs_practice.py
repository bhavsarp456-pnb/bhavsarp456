from threading import Thread
from logging import ERROR, INFO, error, basicConfig, warning
from time import sleep, asctime
def thread_function(name):
    error(f"{asctime()} : thread {name} starting")
    sleep(2)
    error(f"{asctime()} : thread {name} working")
    sleep(3)
    error(f"{asctime()} : thread {name} finishing")

if __name__ == "__main__":
    basicConfig(level=ERROR)
    error(f"{asctime()} : main : before creating threads")
    th1 = Thread(target=thread_function, args=(1,))
    th2 = Thread(target=thread_function, args=(2,))
    error(f"{asctime()} : main : beofre running threads")
    th1.start()
    th2.start()
    sleep(3)
    error(f"{asctime()} : main : before joining threads")
    th1.join()
    th2.join()