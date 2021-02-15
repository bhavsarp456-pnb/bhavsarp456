#race condition
from threading import Thread
x = 0
#increment function
def increment_global():
    global x #takes the global variable
    x += 1#increment the number
    
def taskofThread():#threaad function
    for i in range(50000):
        increment_global()

def main():
    t1 = Thread(a = taskofThread)#defines t1 as a task 1 of the process
    t2 = Thread(a = taskofThread)#defines t2 as a task 2 of the process
    t1.start()#this will start the process of task 1
    t2.start()#tihs will start the process of task 2

if __name__ == "__main__":
    for f in range(1,6):
        main()
        print(f"x = {x} after iteration {f}")