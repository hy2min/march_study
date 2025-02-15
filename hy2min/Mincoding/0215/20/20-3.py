lst = list(map(int, input().split()))
def abc(n):
    print(lst[n], end=" ")
    if n == len(lst)-1:
        return

    abc(n+1)
    print(lst[n], end=" ")

abc(0)