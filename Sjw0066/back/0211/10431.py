
# 진짜로 자리 바꾸고 자리 바꾼만큼 더하기

P=int(input())

for tc in range(1,P+1):
    students=list(map(int,input().split()))
    testcase=students.pop(0)

    answer=0
    for i in range(1,len(students)):
        cnt=0
        for j in range(0,i):
            
            if students[i] > students[j]:
                break

            if students[i] < students[j]:
                cnt+=1
            
        if cnt:
            students[i] ,students[i-cnt] = students[i-cnt] , students[i]
            answer += cnt

    print(testcase,end=" ")
    print(answer)


# 버블 정렬하고 그 횟수 구하기
'''
def bubble_sort(lst): 
    global cnt
    for i in range(len(lst)-1, 0, -1) : 
        for j in range(i) :
            if lst[j] > lst[j+1] :
                lst[j], lst[j+1] = lst[j+1], lst[j] 
                cnt += 1

T = int(input())

for _ in range(T):
    students=list(map(int,input().split()))

    testcase=students.pop(0)

    cnt = 0

    bubble_sort(students)

    print(testcase, cnt)
'''