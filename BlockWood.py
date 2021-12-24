# Minimum numbers of squre shape without wasting wood
m, n = map(int, input().split())
x = min(m, n)
y = x*x
z = m*n
s = int(z/y)
r = z % y
s = s+r
print(s)
