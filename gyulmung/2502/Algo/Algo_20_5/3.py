string = list(input())

divide_string = len(string) // 2

string1 = string[0:divide_string]
string2 = string[divide_string:len(string)]

if string1 == string2:
    print('동일한문장')
else:
    print('다른문장')