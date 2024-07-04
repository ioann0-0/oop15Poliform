import math

class Square:
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side ** 2

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2

class CircleInSquare(Square, Circle):
    def __init__(self, side):
        Square.__init__(self, side)
        Circle.__init__(self, side / 2)  

def main():
    side_length = 10
    circle_in_square = CircleInSquare(side_length)
    
    print(f"Сторона квадрата: {side_length}")
    print(f"Площадь квадрата: {circle_in_square.area()}")

    print(f"Радиус окружности: {circle_in_square.radius}")
    print(f"Площадь окружности: {circle_in_square.area()}")

if __name__ == "__main__":
    main()
