class MyStatic:
    def reset(self):
        self.x = 0
        self.y = 0


a = MyStatic()
a.reset()
print("a : " , a.x)
print("b : " , a.y)