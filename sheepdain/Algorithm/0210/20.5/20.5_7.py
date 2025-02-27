word=input()
for i in range(len(word)):
    for j in range(i+1):
        print(word[j],end='')
    print()