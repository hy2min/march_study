black=list(input())
town=[['C','D','A'],['B','M','Z'],['Q','P','O']]

cnt=0
for i in black:
    for j in town:
        if i in j :
            cnt+=1
print(f'{cnt}명')