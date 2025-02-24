arr = list(input())
def abc(idx):
    if idx == 5:
        print()
        return
    print(arr[idx], end='')
    abc(idx+1)
    print(arr[idx], end='')

abc(0)