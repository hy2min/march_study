st = input()
start = 0
end = len(st) - 1
per = -1
while start <= end : 
    mid = (start + end) // 2
    if st[mid] == '#' : 
        per = mid
        start = mid + 1
    else : 
        end = mid - 1

# while start <= end : 
#     mid = (start + end) // 2
#     if st[mid:mid+2] == '#_' : 
#         per = mid
#         break
#     elif st[mid:mid+2] == '##' : 
#         start = mid + 1
#     else : 
#         end = mid - 1

# if per == -1 : 
#     per = len(st) -1

print(f'{(per+1)*10}%')