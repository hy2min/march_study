line1=[5,2,7,-5,-7,9]
line2=[4,-5,-7,9,-5,3]

visited1 = [0]*6
visited2 = [0]*6

Min = 1e8
ret = 0

def dfs(cnt, Sum):
    global Min, ret
    if abs(Sum) > Min:
        return
    if abs(Sum) <= Min and cnt > 12:
        Min = abs(Sum)
        ret = Sum
        return

    if cnt % 2 == 1:
        for i in range(6):
            if visited1[i] == 0:
                visited1[i] = 1
                Sum += line1[i] * cnt
                cnt += 1
                dfs(cnt, Sum)
                visited1[i] = 0

    else:
        for i in range(6):
            if visited2[i] == 0:
                visited2[i] = 1
                Sum += line2[i] * cnt
                cnt += 1
                dfs(cnt, Sum)
                visited2[i] = 0
dfs(1, 0)
# print(Min)
print(ret)