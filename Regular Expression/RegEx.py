import re
str1 = "rohan Python Rstforum"
str2 = "RRRRohan Python"
str3 = "RRRRRohan Pythonnnnnnn"
str4 = "Rohan12345!@#$!@#$ Python"
str5 = "Rohan   Python"
str6 = "rohan@123 and amit@456 are the 2 IDS"
str7 = ''' Welcome to
RST Forum'''
str8 = 'My PC has ip 192.16.7.1 and yours has 1.1.1.1'
str9 = "rohan+Python"
x = re.findall("[a-z]+@\d\d\d",str6)
y = re.match(".+",str7,re.DOTALL)
z = re.findall("\d{1,3}.\d{1,3}.\d{1,3}",str8)
a = re.match("rohan\+Python",str9)
b = re.match("rohan.+",str5,re.I)
print(y.group())
print(x)
print(str7)
print(z)
print(a.group())
print(b.group())