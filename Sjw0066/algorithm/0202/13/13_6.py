arr= [[4,5,6,1,3,1],[2,1,3,6,3,6]]
def main():
    global result_a,result_b,result_c
    Input()
    result_a,result_b,result_c=Process(a,b,c)
    Output(result_a,result_b,result_c)

def Input():
    global a,b,c
    a,b,c=list(map(int,input().split()))

def Process(a,b,c):
    cnt_a=0
    cnt_b=0
    cnt_c=0
    for i in arr:
        for j in i:
            if j == a :
                cnt_a+=1
            elif j==b :
                cnt_b+=1
            elif j==c :
                cnt_c+=1
    return cnt_a,cnt_b,cnt_c

def Output (result_a,result_b,result_c):

    print(f'{a}={result_a}개')
    print(f'{b}={result_b}개')
    print(f'{c}={result_c}개')
   

main()