juso = [402,401,302,301,202,201,102,101]
name = [
    ['K','I','M',0,0],
    ['T','E','A',0,0],
    ['S','O','M',0,0],
    ['O','P','P','O',0],
    ['T','O','M',0,0],
    ['G','D','K',0,0],
    ['J','A','M','E',0],
    ['M','I','N',0,0],
]

a = int(input())

for i in range(8):
    if juso[i] == a:
        result = i

for i in range(5):
    if name[result][i] != 0:
        print(name[result][i],end='')