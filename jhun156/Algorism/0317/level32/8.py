N = int(input())
arr = [input() for _ in range(N)]

def check(string):

    a = string.capitalize()
    b = string.lower()
    c = string.upper()
    if string == a:
        return a
    elif string == b:
        return a
    else:
        return c

for i in range(N):
    arr[i] = check(arr[i])

arr.sort()
print('\n'.join(arr))