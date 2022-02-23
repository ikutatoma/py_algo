import re
l = int(input())
a = input(1).split(' ')
def bubbleSort(a):
    flag = 1
    i =0
    while flag:
        flag = 0
        for j in reversed(range(1+i,l)):

            if int(re.sub(r"\D", "", a[j])) < int(re.sub(r"\D", "", a[j-1])):
                a[j],a[j-1] = a[j-1],a[j]
                flag = 1
        i+=1
    print(a)

def selectionSort(a):
    for i in range(l):
        minj = i
        for j in range(i,l):
            if(int(re.sub(r"\D", "", a[j])) < int(re.sub(r"\D", "", a[minj]))):
                minj = j
        a[i],a[minj] = a[minj],a[i]
    print(a)

bubbleSort(a)
selectionSort(a)