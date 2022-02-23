def insertionSort(A,n,g):
    for i in range(g,n):#g=4,n=10,i=4,5...9
        v = A[i] # g=4,n=10 v= A[4],A[5]...A[9]
        j = i - g #g=4,n=10 j=0,1...5
        while j >= 0 and A[j] > v:
            A[j+g] = A[j]
            j -= g
        A[j+g] = v
    print(A)

def shellSort(A,n):
    G = [4,3,1]
    m = len(G)
    for i in range(m):
        insertionSort(A,n,G[i])

n = int(input())
A = [int(input()) for i in range(n)]
shellSort(A,n)

"""
10
4
8
9
1
10
6
2
5
3
7
"""




