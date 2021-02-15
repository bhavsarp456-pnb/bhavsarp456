#Write a python script to check whether a given number is prime or not.
num = int(input("num:"))
if num > 1:
    for prime in range(2,10):
        if num % prime == 0:
            print(f"{num} is not a prime number.")
            break
    else:
        print(f"{num} is a prime number.")
        
else:
    print(f"{num} is not a prime number")
