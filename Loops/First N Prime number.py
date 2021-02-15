N = int(input("Enter the N Number:"))
if N > 1:
    for num in range(1,N+1):
        count = 0
        for i in range(2,num):
            if num % i == 0:
                count += 1
                break
                
        if count == 0 and num != 1:
            print(num,end=" ")