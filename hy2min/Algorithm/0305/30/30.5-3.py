import heapq

arr = [1,5,4,2,-5,-7]
n = int(input())

ans = heapq.nlargest(n,arr)[-1]
print(ans)
# arr.sort(reverse=True)
# print(arr[n-1])


