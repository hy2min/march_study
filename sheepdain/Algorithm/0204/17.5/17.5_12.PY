arr=[
    ['A','B','C','D','E'],
    ['F','G','H','I','J'],
    ['K','L','M','N','O'],
    ['P','Q','R','S','T'],
    ['U','V','W','X','Y']
]
a=input()
def isFind(a):
    for i in range(5):
        for j in range(5):
            if arr[i][j]==a:
                return f'{i-2},{j-2}'
print(isFind(a))