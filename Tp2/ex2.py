#Write a Python program that reads the width and height of a rectangle and calculates its perimeter and area.
class rectangle:
    def __init__(self, width , height):
        self.wid= width
        self.hei=height
    def perimeter(self):
        return 2*(self.wid + self.hei)
    def area(self):
        return self.hei* self.wid
Height = int(input(" Please enter height :"))
width =int(input("Enter width :"))
Recipe= rectangle(Height , width)
print("Perimeter:", Recipe.perimeter())
print("Area:", Recipe.area())

