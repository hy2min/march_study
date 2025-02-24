man = 1
for _ in range(5) : 
    if input() == 'up' : 
        man += 1
    else : 
        man -= 1

if man > 0 : 
    print(man)
else : 
    print(f'B{-man+1}')