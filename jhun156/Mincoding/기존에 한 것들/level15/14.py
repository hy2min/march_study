arr = [
    ['P','O','T','I','O'],
    ['A','B','C','D','E'],
    ['Y','O','U','R','E'],
]

a,b = map(int,input().split())

string = ''

for i in range(3):
    for j in range(a,b+1):
        string += arr[i][j]
    
print(string)