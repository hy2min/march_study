for tc in range(1, 11) : 
    dump = int(input())
    box_list = list(map(int, input().split()))
    for i in range(dump) : 
        max(box_list) -= 1
        min(box_list) += 1
                
    print(f'#{tc} {max(box_list)-min(box_list)}')