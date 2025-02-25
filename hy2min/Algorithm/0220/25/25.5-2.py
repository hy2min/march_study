s = input()

num = ''
ret = 0

for i in s:
    if i.isdigit():
        num += i
    elif i == '[':
        if num:
            num=''

    elif i == '{}':
        if num:
            num=''

    elif i == ']':
        val = int(num)
        ret += val
        num = ''

    elif i == '}':
        val = int(num)
        ret *= val
        num = ''

print(ret)