name1=input()
name2=input()
name3=input()

def compare(name1,name2,name3):
    flag=0
    for i,j,k in zip(name1,name2,name3):
        if i==j and i==k and j==k:
            flag+=1

    if flag==len(name1):
        print("YES")
    else:
        print("NO")


compare(name1,name2,name3)

"""
2번째 풀이
name1=input()
name2=input()
name3=input()

if name1==name2 and name2==name3 and name1==name3:
    print("YES")
else:
    print("NO")

"""