Year = int(input("Enter the year:"))
print(f"{Year}is a leap year"if (Year%4) == 0 elif (Year%100) == 0 elif (Year%400) == 0 else f"{Year}Not a Leap Year")