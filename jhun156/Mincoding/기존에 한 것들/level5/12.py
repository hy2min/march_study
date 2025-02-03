def QTR():
    print("QTR100%")

def BBQ():
    print("BBQ100%")

a,b,c = map(int,input().split())

sum = a + b + c

if sum >= 10:
    QTR()
else:
    BBQ()

