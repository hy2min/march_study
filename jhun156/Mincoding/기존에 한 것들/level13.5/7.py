arr = [
    ['D','A','S'],
    ['Q','W','V'],
    ['R','T','Y'],
]

def main():
    y1,x1 = map(int,input().split())
    y2,x2 = map(int,input().split())
    A = Find(y1,x1)
    B = Find(y2,x2)
    print(A,B)

def Find(y,x):
    global arr
    result = arr[y][x]
    return result

main()