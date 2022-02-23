l = int(input())
a = input(1).split(' ')

for i in range(1,l):
    v = a[i]
    j = i-1
    while j>=0 and a[j]>v:
        a[j+1] = a[j]
        j-=1
    a[j+1] =v
    print(a)

# 6
# 5 2 4 6 1 3


