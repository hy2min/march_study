T = int(input())
for tc in range(1, T+1):
    data = input().split()
    N = int(data[0])
    robots = {
        'O' : {'time' : 0, 'location' : 1},
        'B' : {'time' : 0, 'location' : 1},
    }
    
    real_time = 0

    for i in range(1, 2*N, 2) : 
        robot = data[i]
        button = int(data[i+1])
        
        location = robots[robot]['location']
        last_time = robots[robot]['time']
        
        move = abs(button - location)
        
        wait_time = real_time - last_time
        
        real_move = max(0, move - wait_time)
        
        real_time += real_move + 1

        robots[robot]['time'] = real_time
        robots[robot]['location'] = button

    print(f'#{tc} {real_time}')