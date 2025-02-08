class sketchbook : 
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def mix(self) : 
        return ''.join(sorted(set(self.a+self.b+self.c)))        

arr = [input() for _ in range(3)]
image = sketchbook(*arr)
ret = image.mix()
print(ret)