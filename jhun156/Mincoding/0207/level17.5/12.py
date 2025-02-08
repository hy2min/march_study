arr = [
    ['A','B','C','D','E'],
    ['F','G','H','I','J'],
    ['K','L','M','N','O'],
    ['P','Q','R','S','T'],
    ['U','V','W','X','Y'],
]

def Find_xy(chr):
    for i in range(5):
        for j in range(5):
            if arr[i][j] == chr:
                return i-2,j-2

a = input()
y,x= Find_xy(a)
print(f"{y},{x}")