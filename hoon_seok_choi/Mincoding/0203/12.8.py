arr = [[0] * 3 for _ in range(3)]  
a = input()

if '0' <= a <= '9': 
    n = 6
    for i in range(3):
        for j in range(i, 3): 
            arr[i][j] = n
            n -= 1

elif 'A' <= a <= 'Z': 
    n = 6
    for i in range(3): 
        for j in range(i + 1): 
            if i == 0:
                arr[i][j] = 6   
            elif i == 1:
                arr[i][j] = 4+j  
            else:
                arr[i][j] = 1+j


for i in range(3):
    for j in range(3):  
        if arr[i][j] == 0 :
            arr[i][j] = " "
        print(arr[i][j], end="")
    print()



'''
하나는 for문 돌리면서 if
또하나 2중 for 
654
32
1

654
 32
  1

6
45
123

cnt 써서 0 부터 줄어들게끔 

2중포문으로 
규칙을 먼저 찾아야함, 

if문 i+j 가 3보다 작을때 
역배열 이나 뒤에서부터 

if 문은 채우지 않고 
아래서부터 채워도 되고 
i가 1일때 j는 0 
'''