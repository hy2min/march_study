a,b,c = [input() for _ in range(3)]
arr = [a,b,c]

flag = 0


for i in range(len(arr)) :
    if 'M' in arr[i] :
        print("M이 존재합니다")
        break 
    else :
        print("M이 존재하지 않습니다")