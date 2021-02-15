#Write a python script to print next prime number of a given number. 
num = int(input("Enter the number:"))

if num > 1:
    for i in range(2,num):
        if num % i == 0:
            num += 1
    else:
        print(f"next prime number:{num}")
else:
    print(f"{num}:Not a prime number.")
