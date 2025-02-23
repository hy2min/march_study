def dfs(level,result,win,lose):
    if level == 3:
        if lose == 0:
            print(f'{win}승({result})')
            return
        if win == 0:
            print(f'{lose}패({result})')
            return
        print(f'{win}승{lose}패({result})')
        return

    dfs(level+1,result +'승',win+1,lose)
    dfs(level+1,result +'패',win,lose+1)

dfs(0,'',0,0)
