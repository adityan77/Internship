# Create a Rectangle Class
# Attributes: length, width.

# Methods:

# area() — Returns the area of the rectangle.

# perimeter() — Returns the perimeter.

# Test it: Create a few instances and print their area and perimeter.
class Rectanle:
    def __init__(self,len,wid):
        self.len=len
        self.wid=wid
    def area(self):
        area=self.len*self.wid 
        print(area)
    def perimeter(self):
        per=2*(self.len+self.wid)
        print(per)
l=float(input("Enter Length Of Rectangle:-"))
w=float(input("Enter Width Of Rectangle:-"))
Rect=Rectanle(l,w)
Rect.area()
Rect.perimeter()