class Robot:
    def __init__(self,a,b,t):
        self.a = a
        self.b = b
        self.t = t

a,b,t = input().split()

robert = Robot(int(a),int(b),t)

print(robert.a + robert.b, end=" ")
print(robert.t)