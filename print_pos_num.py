list1 = [12, -7, 5, 64,-14]
output = []

list2 = [12, 14, -95, 3]

for each in list1:
    if(int(each)) > 0:
        output.append(each)
    else:
        continue

print(output)

output2 = []

for each in list2:
    if(int(each)) > 0:
        output2.append(each)
    else:
        continue

print(output2)
