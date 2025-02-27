admin_id='qlqlaqkq'
admin_pw='tkaruqtkf'

user_id=input()
user_pw=input()

def login(id,pw):
    if len(id) == len(admin_id):
        for i in range(len(admin_id)):
            if admin_id[i] != id[i]:
                return 0
    else:
        return 0

    if len(pw) == len(admin_pw):
        for i in range(len(admin_pw)):
            if admin_pw[i] != pw[i]:
                return 0
    else:
        return 0
    return 1

result=login(user_id,user_pw)
if result:
    print("LOGIN")
else:
    print("INVALID")