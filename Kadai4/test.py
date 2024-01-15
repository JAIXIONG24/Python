list_a = [20, 20, 20, 20]
list_b = [1, 2,3,4]

sum_a = sum_b = 0
for i in range(len(list_a)):
    sum_a += list_a[i]
    sum_b += list_b[i]

print(sum_a)
print(sum_b)

sum = sum_a + sum_b

print(sum)