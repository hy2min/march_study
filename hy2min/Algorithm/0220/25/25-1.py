before = ['KFC','MC','BICMAC','SHACK','SONY']
after = ['#BBQ#','#BBQ#','#MACBOOK#','#SHOCK#','#NONY#']

s = input()
for i in range(len(before)):
    s = s.replace(before[i],after[i])

print(s)