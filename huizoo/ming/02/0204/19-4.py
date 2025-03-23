class Data : 
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


a = Data(*map(int, input().split()))
b = Data(*map(int, input().split()))

print(a.x+b.x)
print(a.y+b.y)
print(a.z+b.z)

# class Data : 
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z

# a_input = list(map(int, input().split()))
# b_input = list(map(int, input().split()))
# a = Data(*a_input)
# b = Data(*b_input)

# print(a.x+b.x)
# print(a.y+b.y)
# print(a.z+b.z)