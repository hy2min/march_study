class MC : 
    def __init__(self, burger1, burger2):
        self.burger1 = burger1
        self.burger2 = burger2

burgers = [input() for _ in range(4)]

bob = MC(*burgers[:2])
tom = MC(*burgers[2:])

# print(f'bob.burger{1}={len(bob.burger1)}')
# print(f'bob.burger{2}={len(bob.burger2)}')
# print(f'tom.burger{1}={len(tom.burger1)}')
# print(f'tom.burger{2}={len(tom.burger2)}')

for i in range(2) :    
    print(f'bob.burger{i+1}={len(getattr(bob, f"burger{i+1}"))}')

for i in range(2) :    
    print(f'tom.burger{i+1}={len(getattr(tom, f"burger{i+1}"))}')
