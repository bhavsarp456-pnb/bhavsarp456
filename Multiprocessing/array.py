from multiprocessing import Array, Value, Process

def square_list(list,r,ss):
    for index, num in enumerate(list):
        r[index] = num * num
    ss.value = sum(r)
    return ss.value

if __name__ == "__main__":
    mylist = [1,2,3,4]
    result = Array('i',len(mylist))
    square_sum = Value('i')
    
    p1 = Process(target = square_list, args=(mylist, result, square_sum))

    p1.start()
    p1.join()

    print(f"Result: {result[:]}")
    print(f"Square Sum: {square_sum}")