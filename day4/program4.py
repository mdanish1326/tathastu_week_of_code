sizeDic = int(input("Enter Size of Dictionary: "))

dic = dict()
for i in range(sizeDic):
    k = input("Enter key of element "+str(i+1)+" : ")
    v = int(input("Enter value to above key:"))
    dic[k] = v

output = dict()
for k, v in dic.items():
    if v not in output.values():
        output[k] = v

print("after removing duplicate value the dic is: ", output)
