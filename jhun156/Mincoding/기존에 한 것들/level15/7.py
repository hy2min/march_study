arr = ['A','B','C','Z','E','T','Q']

lst = list(input())

for i in lst:
    if i in arr:
        print(f"{i}=마을사람")
    else:
        print(f"{i}=외부사람")
