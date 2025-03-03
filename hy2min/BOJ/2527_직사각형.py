for _ in range(4):
    x1,y1,p1,q1,x2,y2,p2,q2 = map(int, input().split())

    # 겹치지 않는 경우
    if x1 > p2 or x2 > p1 or y1 > q2 or y2 > q1:
        print('d')
    
    # 선이 겹치는 경우
    elif x1 == p2 or x2 == p1:
        if y1 == q2 or y2 == q1:    
            print('c')
        else:
            print('b')
    elif y1 == q2 or y2 == q1:
        print('b')
    
    # 겹쳐서 직사각형이 만들어지는 경우
    else:
        print('a')