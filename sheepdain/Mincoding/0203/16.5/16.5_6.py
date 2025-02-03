s=input()
def maxIndex(s):
    arr=[]
    for i in s:
        arr.append(ord(i))
    MAX=max(arr)
    for i in range(len(arr)):
        if arr[i]==MAX:
            return i
def minIndex(s):
    arr=[]
    for i in s:
        arr.append(ord(i))
    MIN=min(arr)
    for i in range(len(arr)):
        if arr[i]==MIN:
            return i

print(maxIndex(s))
print(minIndex(s))
