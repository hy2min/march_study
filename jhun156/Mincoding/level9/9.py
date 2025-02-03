arr = [
    ['F','E','W'],
    ['D','C','A'],
]

def main():
    a = input()
    return a

def findCh(chr):
    
    cnt = 0

    for i in range(2):
        for j in range(3):
            if arr[i][j] == chr:
                cnt = 1
                break

    if cnt == 1:
        print("발견")
    else:
        print("미발견")

findCh(main())