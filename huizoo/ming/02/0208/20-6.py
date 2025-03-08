a, b = map(int, input().split())
def atob(n1, n2) : 
    print(n1, end = ' ')
    if n1 < n2 : 
        atob(n1+1, n2)
        print(n1, end = ' ')

atob(a, b)