friends = ['E','W','A','B','C']
boat = []
def dfs(level, max_level) : 
    if level == max_level : 
        print(''.join(boat))
        return
    for friend in friends : 
        if friend != exception :
            if friend not in boat : 
                boat.append(friend)
                dfs(level+1, max_level)
                boat.pop()

exception = input()
dfs(0, 4)