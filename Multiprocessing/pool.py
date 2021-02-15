from multiprocessing import Pool
from os import getpid
from time import sleep

def square(n):
    print(f"Worker process id for {n}:{getpid()}")
    sleep(3)
    return (n * n)

if __name__ == "__main__":
    mylist = [1,2,3,4,5,6,7,8]
    p = Pool(4)
    result = p.map(square,mylist)
    print(result)