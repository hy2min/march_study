# arr = list(map(str, input().split()))
arr = [*input()]
a = int(input())
arr.insert(a,'A')


print(*arr,sep="")