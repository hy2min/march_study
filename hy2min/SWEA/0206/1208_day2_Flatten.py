for idx in range(10):
    dump_n = int(input())
    boxes = list(map(int, input().split()))

    for _ in range(dump_n):
        max_idx = boxes.index(max(boxes))
        min_idx = boxes.index(min(boxes))
        boxes[max_idx] -= 1
        boxes[min_idx] += 1

    print(f'#{idx+1} {max(boxes)-min(boxes)}')
