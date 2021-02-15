from time import sleep
from threading import Thread

def paanipoori():
    print("Paani")
    sleep(3)
    print("Poori")

t1 = Thread(target = paanipoori)
t2 = Thread(target = paanipoori)
t3 = Thread(target = paanipoori)

t1.start()
t2.start()
t3.start()