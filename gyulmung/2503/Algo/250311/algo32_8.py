import sys
sys.stdin=open('input.txt','r')

def Big():
    global name
    for i in range(len(name)):
        if ord(name[i]) < 97:
            continue
        else:
            name[i] = chr(ord(name[i])-32)

n = int(input())
members = []
for i in range(n):
    name = list(input())
    for j in range(1, len(name)):
        if 'A' <= name[0] <= 'Z':
            if 'A' <= name[j] <= 'Z':
                Big()
                break
        elif 'a' <= name[0] <= 'z':
            if 'A' <= name[j] <= 'Z':
                Big()
                break
            else: name[0] = chr(ord(name[0])-32)
    member = ''.join(name)
    members.append(member)
members.sort()
for i in members:
    print(i)