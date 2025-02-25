# DAT 만들기
# DAT[i]가 0이 아닐때 len(DAT[i])만큼 출력하기
# 오늘 배운 거 다른방식

arr = [
    ['A','B','C'],
    ['A','G','H'],
    ['H','I','J'],
    ['K','A','B'],
    ['A','B','C'],
]

DAT = [0] * 27

for i in range(5):
    for j in range(3):
        DAT[ord(arr[i][j])-65] += 1

# DAT는 해당 인덱스에 해당하는 개수임 DAT[0] = 4 / A가 4개

for i in range(27):
    if DAT[i] != 0:
        for j in range(DAT[i]):
            print(chr(i+65),end='')