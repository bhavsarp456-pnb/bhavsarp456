
def is_leap(year):
    if year % 4 == 0 or year % 400 == 0 and year % 100 != 0:
        return True
    return False
    
year = int(input())
print(is_leap(year))
# Python Program to Check Leap Year using If Statement

year = int(input("Please Enter the Year Number you wish: "))

if (( year%400 == 0)or (( year%4 == 0 ) and ( year%100 != 0))):
    print("%d is a Leap Year" %year)
else:
    print("%d is Not the Leap Year" %year)
    