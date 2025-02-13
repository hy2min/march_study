import sys
sys.stdin = open("input.txt","r")

def Triangle_of_Pascal(num):



T = int(input())
for tc in range(1,T+1):
    N = int(input())
    Triangle_of_Pascal(N)