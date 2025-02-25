string = input()
nums = []
num = ''
operator = []

# 음수로 시작할 경우
if string[0] == '-':
    num += '-'
    string = string[1:]

for s in string:
    if s.isdigit():
        num+=s
    else:
        nums.append(int(num))
        operator.append(s)
        num = ''

nums.append(int(num))

ret = nums[0]
for i in range(len(operator)):
    if operator[i] == '+':
        ret += nums[i+1]
    else:
        ret -= nums[i+1]

print(ret)
