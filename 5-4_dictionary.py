import io
import sys
__INPUT = """\
6
insert AAA
insert AAC
find AAA
find CCC
insert CCC
find CCC
"""
sys.stdin = io.StringIO(__INPUT)

M = 100
NIL = (-1)
# L = 14
H = [0]*M
def get_char(ch):
    if ch == 'A':
        return 1
    elif ch == 'C':
        return 1
    elif ch == 'G':
        return 1
    elif ch == 'T':
        return 1
    return 0

def get_key(str):
    sum = 0
    p = 1
    for i in range(len(str)):
        sum += p*(get_char(str[i]))
        p *= 5
    return sum

def h1(key):
    return key % M

def h2(key):
    return 1 + (key % (M-1))

def find(str):
    key = get_key(str)
    i =0
    while i >=0:
        h = (h1(key) + i*h2(key))%M
        if H[h] == str:
            return 1
        elif H[h] == 0:
            return 0
        i+=1
    return 0

def insert(str):
    key = get_key(str)
    i = 0
    o = 0
    while i>=0:
        h = (h1(key) + i*h2(key))%M
        if H[h] == str:
            return 1
        elif H[h]== 0:
            H[h] = str
            return 0
        i+=1
    return 0

n = int(input())
for i in range(n):
    com,str = input().split(' ')
    com = list(com)
    str = list(str)
    if com[0] == 'i':
        insert(str)
    else:#find
        print('yes') if find(str) else print('no')
