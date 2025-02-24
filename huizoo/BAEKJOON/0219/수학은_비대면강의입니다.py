import sys
a, b, c, d, e, f = map(int, sys.stdin.readline().split())
print(int((e*c-b*f)/(a*e-b*d)), int((d*c-a*f)/(d*b-a*e)))