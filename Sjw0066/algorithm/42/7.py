name={'a':15,'b':20,'c':44,'d':22,'e':55,'f':16,'g':45}

gbab=input()
n=int(input())

gprice=0

for i in gbab:
    gprice+=name[i]
Max=-21e8

def dfs(level,Sum):
    global Max

    if level==n:
        if str(Sum)[-1]=='0':
            if Max<Sum:
                Max=Sum
        return
    for i in gbab:
        dfs(level+1,Sum-name[i])

dfs(0,gprice)
print(Max)