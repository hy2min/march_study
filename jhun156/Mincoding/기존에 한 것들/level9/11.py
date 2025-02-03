# a = [i for i in map(int,input().split())]
# b = [i for i in map(int,input().split())]

# arr = list(zip(a,b))
# for i in range(2):
#     print(sum(arr[i])//2, end = ' ')

arr = [i for i in map(int,input().split())]

a = (arr[0]+arr[2])//2
b = (arr[1]+arr[3])//2
print(a,b)