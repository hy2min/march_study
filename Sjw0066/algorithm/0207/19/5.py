class MC:
    def __init__(self,burger1,burger2):
        self.burger1=burger1
        self.burger2=burger2

input1=input()    
input2=input()    
input3=input()    
input4=input()

bob=MC(input1,input2)
tom=MC(input3,input4)



print(f'bob.burger1={len(bob.burger1)}')   
print(f'bob.burger2={len(bob.burger2)}')   
print(f'tom.burger1={len(tom.burger1)}')   
print(f'tom.burger2={len(tom.burger2)}')   
