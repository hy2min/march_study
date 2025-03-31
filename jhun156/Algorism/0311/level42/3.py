string = input()
n = len(string)
arr = ['BTS','SBS','BS','CBS','SES']
Min = 10000

def dfs(level,sentence):

    global Min
    if len(sentence) > n:
        return
    if sentence == string:
        Min = min(level,Min)
        return

    for i in range(5):
        dfs(level+1,sentence+arr[i])

dfs(0,'')
print(Min)