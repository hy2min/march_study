password = [3 ,7, 4, 9]
pw_input = list(map(int, input().split()))
def isSame():
    if password == pw_input:
        print('pass')
    else:
        print('fail')
isSame()