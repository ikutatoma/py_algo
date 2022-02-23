l = input()
r = [int(input()) for i in range(int(l))]
minv = r[0]
maxv = -20000000000
for j in range(1,len(r)-1):
    maxv = max(r[j] - minv,maxv) 
    minv = min(r[j],minv)
print( '最大の利益は'+ str(maxv))

# 6
# 5
# 3
# 1
# 3
# 4
# 3