class A :
    product={'딸기':300,"메론":500,"수박":1000}
    @classmethod
    def avg_price(cls):
        avg=(cls.product['딸기']+cls.product['메론']+cls.product['수박'])//3
        print(avg)

class B :
    product={'딸기':450,"메론":450,"수박":900}
    @classmethod
    def avg_price(cls):
        avg=(cls.product['딸기']+cls.product['메론']+cls.product['수박'])//3
        print(avg)
class C :
    product={'딸기':200,"메론":150,"수박":700}
    
    @classmethod
    def avg_price(cls):
        avg=(cls.product['딸기']+cls.product['메론']+cls.product['수박'])//3
        print(avg)


a= input()

if a=='A':
    A.avg_price()
elif a == 'B':
    B.avg_price()
elif a=='C':
    C.avg_price()