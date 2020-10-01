import math

X=tuple(map(int, input().split()))
Y=tuple(map(int, input().split()))
x1, y1, z1 = X
x2, y2, z2= Y
D= math.sqrt(((x2-x1)**2)+((y2-y1)**2)+((z2-z1)**2))
print(D)