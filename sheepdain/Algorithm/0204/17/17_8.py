arr=['B','T','K','I','G','Z']
target=list(map(str,input().split()))
def Count(a):
    for i in arr:
        if i==a:
            return 1
    return 0
count=0
for i in target:
    count+=Count(i)
print(count)