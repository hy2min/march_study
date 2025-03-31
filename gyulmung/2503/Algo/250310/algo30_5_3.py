import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
arr = [1, 5, 4, 2, -5, -7]

level = sorted(arr)

print(level[(-N)])