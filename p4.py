class Rectangle:
    def __init__(self,height,width):
        self.height=height
        self.width=width
    def area(self):
       x= self.width*self.height
       return x
rect=Rectangle(4,5)
rect.area()
print(rect.area())

