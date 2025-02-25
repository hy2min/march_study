# import sys
# sys.stdin = open("input.txt","r")

T = 10
for test_case in range(1, T + 1):
    num = int(input())
    input_list = [i for i in map(int,input().split())]
    main_list = [0,0,*input_list,0,0]
    def get_point(index):
        temp_list = [main_list[index + i] for i in range(5)]
        result_list = temp_list[:]
        for i in range(4):
            for j in range(i+1,5):
                if temp_list[i] > temp_list[j]:
                    temp_list[i],temp_list[j] = temp_list[j],temp_list[i]
        temp = result_list[2] - temp_list[3]
        if temp > 0:
            return temp
        else:
            return 0

    answer = 0
    for i in range(num):
        answer += get_point(i)

    print(f"#{test_case} {answer}")