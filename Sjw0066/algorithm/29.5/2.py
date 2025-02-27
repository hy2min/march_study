evid=[-1,0,0,1,2,4,4]
timeStamp=[8,3,5,6,8,9,10]

def abc(index):

    if index==0:
        print('0번index(출발)')
        return

    abc(evid[index])
    print(f'{index}번index({timeStamp[index]}시)')



n=int(input())

abc(n)