import re
my_regex_str = "Ethernet Routing Switch 3549GTS-PWR+"
#Q.16
a = re.findall(r"(.{5}).+ (.+?)\s(\d{2,4}).+-(.{4})", my_regex_str)
print(a[0][0])
#Output - Ether
#Q.17.
print(a[0][1])
#Output - Switch
#Q.18
print(a[0][2])
#Output - 3549
#Q.19
print(a[0][3])
#Output - PWR+
#Q.20
print(a)
#Output - [('Ether', 'Switch', '3549', 'PWR+')]