l = int(input())
a = input(1).split(' ')
flag = 1
sw = 0
i = 0
while flag:
    flag = 0
    for j in reversed(range(i+1,l)):
        if a[j]< a[j-1]:
            a[j],a[j-1] = a[j-1],a[j]
            flag = 1
            sw += 1
    i+=1
print(a)
print(sw)

# 5
# 5 3 2 4 1