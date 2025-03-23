movement = list(map(int, input().split()))

def Michael_Jackson(movement) : 
    print(movement[0], end = ' ')
    if len(movement) > 1 :
        Michael_Jackson(movement[1:])
        print(movement[0], end = ' ')

Michael_Jackson(movement)

# start = 0
# def Michael_Jackson(i) : 
#     print(movement[i], end = ' ')
#     if i < 5 : 
#         Michael_Jackson(i+1)
#         print(movement[i], end = ' ')

# Michael_Jackson(start)
