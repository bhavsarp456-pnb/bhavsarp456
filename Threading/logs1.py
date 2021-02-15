#logs
import threading
import logging
import time
def thread_function(name):
    logging.warning(f"{time.asctime()}: thread {name} starting")
    time.sleep(2)
    logging.warning(f"{time.asctime()}: thread {name} working")
    time.sleep(3)
    logging.warning(f"{time.asctime()}: thread {name} finishing")

if __name__ == "__main__":
    logging.basicConfig(level = logging.WARNING)
    logging.warning(f"{time.asctime()}: main : before creating threads")
    th1 = threading.Thread(target=thread_function, args=(1,))
    th2 = threading.Thread(target=thread_function, args=(2,))
    logging.warning(f"{time.asctime()} : main : before running threads")
    th1.start()
    th2.start()
    time.sleep(3)
    logging.warning(f"{time.asctime()} : main : brefore joining threads")
    th1.join()
    th2.join()