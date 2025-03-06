N, K = map(int, input().split())
room_count = 0

room = [[0]*6 for _ in range(2)]
for _ in range(N) : 
    S, Y = map(int, input().split())
    room[S][Y-1] += 1

for i in range(2) : 
    for j in range(6) : 
        if room[i][j] % K == 0 : 
            room_count += room[i][j] // K
        else : 
            room_count += room[i][j] // K + 1


# room = {
#     '0' : {'1' : 0, '2' : 0, '3' : 0, '4' : 0, '5' : 0, '6' : 0},
#     '1' : {'1' : 0, '2' : 0, '3' : 0, '4' : 0, '5' : 0, '6' : 0},
# }

# for _ in range(N) : 
#     S, Y = input().split()
#     # S == 0 여학생, S == 1 남학생
#     # Y 1 ~ 6학년
#     room[S][Y] += 1


# for i in range(2) :
#     for j in range(6) : 
#         temp_count = room[str(i)][str(j+1)] 
#         if temp_count % K != 0 : 
#             room_count += temp_count//K + 1
#         else : 
#             room_count += temp_count//K

print(room_count)