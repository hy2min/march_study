N=int(input())

lst1=list(map(str,input().split()))
lst1.sort()

 

M=int(input())

order=[]

def find_book(book_name,time,st,ed):
    cnt=0
    time=int(time)
    
    if book_name not in lst1:
        return 'fail'
    
    while 1:
        mid = (st+ed)//2
        if lst1[mid] == book_name:
            cnt+=1
            if cnt>time:
                return 'fail'
            else:    
                return 'pass'
        if lst1[mid] != book_name:
                if (ord(book_name[0])>96 and ord(lst1[mid][0])>96) or (ord(book_name[0])<96 and ord(lst1[mid][0])<96):
                    if ord(book_name[0]) > ord(lst1[mid][0]):
                        cnt+=1
                        ed=mid-1
                    else:
                        cnt+=1
                        st=mid+1
                else:
                    if ord(book_name[0]) < ord(lst1[mid][0]):
                        cnt+=1
                        ed=mid-1
                    else:
                        cnt+=1
                        st=mid+1        
        if st>ed:
            break
    if cnt>time:
        return 'fail'
    else:    
        return 'pass'
            




for i in range(M):
    book_name,S=map(str,input().split())
    order.append([book_name,S])



for i in range(M):
    result=find_book(order[i][0],order[i][1],0,len(lst1)-1)
    print(result)