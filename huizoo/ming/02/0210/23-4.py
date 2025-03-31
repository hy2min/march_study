n = int(input())
members = ['B', 'T', 'S', 'K', 'R']
unit = []

def dfs(level, max_level) : 
    if level == max_level : 
        return 1
    cnt = 0
    for member in members : 
        if member not in unit :
            if len(unit) >= n-1 : 
                if 'S' in unit : 
                    unit.append(member)
                    cnt += dfs(level+1, max_level)
                    unit.pop()  
                elif member == 'S' : 
                    unit.append(member)
                    cnt += dfs(level+1, max_level)
                    unit.pop()
            else : 
                unit.append(member)
                cnt += dfs(level+1, max_level)
                unit.pop()

    return cnt

print(dfs(0, n))


            
        
