class shapes:
    def area(self):
        pass
    def perimeter(self):
        pass
class circle(shapes):
    def area(radius):
        return 3.14 * radius * radius
    def perimeter(radius):
        return 2 * 3.14 * radius
class rectangle(shapes):
    def area(length, width):
        return length * width
    def perimeter(length, width):
        return 2 * (length + width)
class square(shapes):
    def area(side):
        return side * side 
    def perimeter(side):
        return 4 * side   
print(circle.perimeter(int(input("Enter the radius of the circle:"))))