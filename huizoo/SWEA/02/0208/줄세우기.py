P = int(input())
for tc in range(1, P+1) : 
    inputs = list(map(int, input().split()))
    student = inputs[1:]
    line = []
    cnt = 0
    for i in range(20) : 
        line.append(student[i])
        for k in range(len(line)-1, 0, -1) : 
            if line[k] < line[k-1] : 
                line[k], line[k-1] = line[k-1], line[k]
                cnt += 1
    
    print(f'{tc} {cnt}')
    