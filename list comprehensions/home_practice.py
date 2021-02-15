x=[]
nested_list = [["Piyush","bhavsarp456@gmail.com",7208186114],["Kotak Mahindra bank","Goregaon - (West)",450000],["Cricket","Football","Listning Musics"]]
for list in nested_list:
        for details in list:
                x.append(details)

print(x)