#symmetric processing
import multiprocessing

def print_cube(number):
    print(f"Cube : {number**3}")

def print_square(number):
    print(f"Square : {number**2}")

if __name__ == "__main__":
    p1 = multiprocessing.Process(target=print_square, args=(5,))
    p2 = multiprocessing.Process(target=print_cube,args=(5,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Done")