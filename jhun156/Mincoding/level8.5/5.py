a,b,c = input().split()

for j in range(int(c)):
    for i in range(ord(a),ord(b)+1):
        print(chr(i),end='')
    print()