flag = 0
a,b,c = 'a','a','a'
s,t,r = 0,0,0

def custom(A,B,C):
    global a,b,c
    a,b,c = input().split()
    return a,b,c

def process(A,B,C):
    global a,b,c,flag
    if a == 'A' and b == 'B' and c == 'C':
        flag = 1
    
def output():
    global flag
    if flag == 1:
        print("ABC를찾았다")
    else:
        print("못찾았다")

s,t,r = custom(a,b,c)
process(s,t,r)
output()