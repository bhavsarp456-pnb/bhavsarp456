file = open("C:\\Users\\Dell\\OneDrive\\Desktop\\Laptop_List.txt","a+")
file.writelines(['Dell\n','Apple\n','HP\n','Acer\n','Asus\n','Lenevo\n','Toshiba\n'])
file.seek(0)
x = file.readlines()
NewData = [i for i in x if i.startswith("A")]
file2 = open("C:\\Users\\Dell\\OneDrive\\Desktop\\Sorted_Laptop_List.txt","a+")
file2.write("Sorted list is:-\n")
file2.writelines(NewData)
file2.seek(0)
print(file.read())
file2.close()