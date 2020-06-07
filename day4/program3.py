#day4 find secon max in dic (program3)

sizeDic = int(input("Enter Size of Dictionary: "))

dic = dict()
for i in range(sizeDic):
    k = input("Enter key of element "+str(i+1)+" : ")
    v = int(input("Enter value to above key:"))
    dic[k] = v

print(dic)
secondMax = list(sorted(dic.values()))[-2]
print("second largest value is: ",secondMax)
