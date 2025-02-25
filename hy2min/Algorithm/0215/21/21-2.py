admin_id = "qlqlaqkq"
admin_pw = "tkaruqtkf"

id = input()
pw = input()

def abc(n, id, pw):
    if n == len(admin_id):
        if admin_pw == pw:
            print("LOGIN")
        else:
            print("INVALID")    
        return    
    
    if admin_id[n] != id[n]:
        print("INVALID")
        return

    abc(n+1, id, pw)

abc(0, id, pw)