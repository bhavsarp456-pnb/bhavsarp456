def prime(a,b):
    for i in range(a,b+1):
        if i > 1:
            for j in range(2,i):
                if (i % j) == 0:
                    break
            else:
                print(f"{i}:prime number")
prime(2,20)