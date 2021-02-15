n = int(input())
if n % 2 != 0:#odd 
    print("Weird")
if n in range(0,6):
    if n % 2 == 0:# % - remainder
        print("Not Weird")
if n in range(6,21):
    if n % 2 == 0:
        print("Weird")
if n in range(21,50):
    if n % 2 == 0:#even
        print("Not Weird")