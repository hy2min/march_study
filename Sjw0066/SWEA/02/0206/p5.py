T = 10

for tc in range(1, T + 1):
    N=int(input())
    boxes=list(map(int,input().split()))

    def bubble_sort(arr):
        for i in range(len(arr)-1,0,-1):
            for j in range(0,i):
                if arr[j] > arr[j+1]:
                    arr[j],arr[j+1]=arr[j+1],arr[j]
        return arr
    
    def check_break(arr):
        arr=set(arr)
        arr=list(arr)
        if len(arr) < 3:
            return True
        else:
            return False

    answer= 0


    for i in range(N):
        sorted_boxes=bubble_sort(boxes)
        
        sorted_boxes[0] += 1
        sorted_boxes[-1] -= 1
        
        flag=check_break(sorted_boxes)
        if flag :
            break
    
    sorted_boxes = bubble_sort(sorted_boxes)
    answer = sorted_boxes[-1] - sorted_boxes[0]    
    
    print(f'#{tc} {answer}')
    