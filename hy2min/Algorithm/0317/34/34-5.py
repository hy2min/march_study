n = int(input())
def binary(n):
    start = 0
    end = 100
    while start <= end:
        mid = (start + end) // 2
        if mid <= n**0.5 <mid + 1:
            return mid

        if n**0.5 < mid:
            end = mid - 1

        elif n**0.5 > mid:
            start = mid+1

ans = binary(n)
print(ans)