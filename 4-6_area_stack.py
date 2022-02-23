
"""
\\///\_/\/\\\\/_/\\///__\\\_\\/_\/_/\
"""
S1 = []
S2 =[]
sum = 0
ch = list(input())

for i in range(len(ch)):
    if ch[i] == '\\':# '\\'は \ です。
        S1.append(i)
    elif ch[i]== '/' and len(S1)>0:
        j = S1[-1]
        S1.pop()
        sum += i-j
        a = i-j
        while len(S2)>0 and S2[-1]['first']>j:
            a += S2[-1]['second']
            S2.pop()
        S2.append({'first':j,'second':a})

ans =[]
print(S2)
while len(S2) >0:
    ans.append(S2[-1]['second'])
    S2.pop()
ans.reverse()
print(sum)
print(len(ans),end="")
for i in range(len(ans)):
    print(' ' + str(ans[i]),end="")
print('')
