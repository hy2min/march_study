arr=['A','T','K','P','T','C','A','B','C']
a,b=map(str,input().split())

def find_index_front(str1):
    for i in range(len(arr)):
        if str1==arr[i]:
            return i
        
def find_index_back(str1):
    for i in range(len(arr)-1,-1,-1):
        if str1==arr[i]:
            return i
        
f_index=find_index_front(a)
b_index=find_index_back(b)

print(b_index-f_index)
