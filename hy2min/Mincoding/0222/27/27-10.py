import math

w = [0,0]
t = [1,math.sqrt(3)]
h = abs(t[0]-w[0])
w = abs(t[1]-w[1])


ret = math.atan2(h,w)
ret = math.degrees(ret)
print(ret)