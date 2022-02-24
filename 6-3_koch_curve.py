import io
import sys
import math
__INPUT = """\
1
"""
sys.stdin = io.StringIO(__INPUT)

class Point():
    def __init__(self):
        self.x = 0
        self.y = 0

def koch(n,a,b):
    if n == 0:
        return
    s = Point()
    t = Point()
    u = Point()
    th = math.pi * 60 / 180.0

    s.x = (2.0 * a.x + 1.0 * b.x) / 3.0
    s.y = (2.0 * a.y + 1.0 * b.y) / 3.0
    t.x = (1.0 * a.x + 2.0 * b.x) / 3.0
    t.y = (1.0 * a.y + 2.0 * b.y) / 3.0
    u.x = (t.x - s.x) * math.cos(th) - (t.y - s.y) * math.sin(th) + s.x
    u.y = (t.x - s.x) * math.sin(th) + (t.y - s.y) * math.cos(th) + s.y

    koch(n - 1, a, s)
    print(s.x, s.y)
    koch(n - 1, s,u)
    print(u.x, u.y)
    koch(n - 1, u, t)
    print(t.x, t.y)
    koch(n - 1, t, b)


n = int(input())
a = Point()
b = Point()
a.x = 0
a.y = 0
b.x = 100
b.y = 0

print(a.x, a.y)
koch(n, a, b)
print(b.x, b.y)
