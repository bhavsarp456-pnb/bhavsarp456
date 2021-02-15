from threading import Thread
from  logging import WARNING, warning, basicConfig
from time import sleep, asctime
def thread_function(name):
    warning(f"{asctime()} : thread {name} starting")
    sleep(2)
    warning(f"{asctime()} : thread {name} working")
    sleep(3)
    warning(f"{asctime()} : thread {name} finishing")

if __name__ == "__main__":
    basicConfig(level=WARNING)
    warning(f"{asctime()} : main : before creating threads")
    th1 = Thread(target=thread_function, args = (1,))#create thread 1
    th2 = Thread(target=thread_function, args = (2,))#create thread 2
    warning(f"{asctime()} : main : before running threads")
    th1.start()
    th2.start()
    sleep(3)
    warning(f"{asctime()} : main : before joining threads")
    th1.join()
    th2.join()