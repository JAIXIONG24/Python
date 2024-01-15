list1 = [10, 4, 2, 2, 8, 9, 7, 5, 1, 3, 4, 6, 8, 11, 6]
list2 = [10, 5, 5, 4, 4, 6, 6, 2, 1, 2, 7, 7, 9, 8, 4]

xmean = float(sum(list1))/float(len(list1))

ymean = float(sum(list2))/float(len(list2))

print("xmean = ", xmean ,"ymean = ", ymean)
x1 = 0.0
y1 = 0.0

for i in range(len(list1)):
    x1 += float((list1[i]-xmean)*(list2[i]-ymean))
    y1 += float((list1[i] - xmean)**2)
    # a = x1 / y1
    # a += float((list1[i] - xmean)**2)

a = float(x1 / y1)
b = ymean - a*xmean
print("a = ", a , "b = ", b)
print(float(sum(list1)))
print(float(sum(list2)))
print(len(list1))

