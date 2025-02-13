N = int(input()) # 1시간 30분

def game_369(x):
    Ny = str(x)
    count = 0
    for j in range(len(Ny)):
        if int(Ny[j]) % 3 == 0:
            if int(Ny[j]) != 0:
                count += 1
        else:
            count
    return count

for i in range(1, N + 1):
    result = game_369(i)
    if result > 0:
        print('-'*result, end = ' ')
    else:
        print(i, end = ' ')