#Q.2
import re
my_regex_str = '200.10.2.0 255.255.255.0 200.20.5.2 1 205 T#1 S IB 5' 
#a = re.search("(.+?) +\d\d(\d)\.([0-9]{2,})\.([0-9]{1,3})\.(\d) +(.+)1 +(\d{3})\s(\w{1,3}#1\s.+\s\d)", my_regex_str)
a = re.search("(.+?) +(\d\d\d)\.([0-9]{2,})\.([0-9]{1,3})\.(\d)\s(\d{1,3})\.(\d{1,3})\.(\d)\.(\d)\s(\d)\s(\d{1,3}\s\w.\d\s\w\s)(.+? \d)", my_regex_str)
print(a.group(12))
#Output - 200.10.2.0 255.255.255.0 200.20.5.2 1 205 T#1 S IB 5
#Q.3
#print(a.group(1))
#Output - 200.10.2.0
#Q.4
#print(a.group(2))
# Output - 5
# Q.5
#print(a.group(3))
#Output - 255
#Q.6
#print(a.group(4))
#Output - 255
#Q.7
#print