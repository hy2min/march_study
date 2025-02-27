class Product:
    
    def __init__(self):
        self.name=input()
        self.size=int(input())
        self.price=int(input())


a=Product()
b=Product()

print(f'{a.name},{b.name}')
print(f'AverageSize={(a.size+b.size)/2:.0f}')
print(f'AveragePrice={(a.price+b.price)/2:.0f}')
