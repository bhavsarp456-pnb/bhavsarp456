file1 = open("C:\\Users\\Dell\\OneDrive\\Desktop\\hackerRank.txt","r")
print(file1.read())
print(file1.seek(0))
print(file1.read())
print(file1.seek(8))
print(file1.read(9))
print(file1.close())