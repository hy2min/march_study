arr = [
    ['A','D','F'],
    ['Q','W','E'],
    ['Z','X','C'],
]

def find(a):
    y = 0
    x = 0
    for i in range(3):
        for j in range(3):
            if arr[i][j] == a:
                y,x = i,j
    return y,x

def main():
    chr = input()
    Y,X = find(chr)
    print(f"{Y},{X}")

main()