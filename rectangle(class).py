class Rectangle:
    def CalculateArea(self):
        print("Enter height")
        print("Enter width")
        self.s=float(input())
        self.s=float(input())
        area=self.s*self.s
        return(area)
    def CalculatePerimeter(self):
        perimeter=2*self.s+self.s
        return(perimeter)               
c=Rectangle()
x=c.CalculateArea()
y=c.CalculatePerimeter()
print("Area of rectangle is=%f"%(x))
print("Area of perimeter is=%f"%(y))                  
