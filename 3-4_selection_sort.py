l = int(input())
a = input(1).split(' ')
c = 0
for i in range(l):
    minj = i
    for j in range(i,l):
        if a[j] < a[minj]:
            minj = j
    a[i],a[minj] = a[minj],a[i]
    c = c+1 if minj != i else c
print(a)
print(c)
# 6
# 5 6 4 2 1 3