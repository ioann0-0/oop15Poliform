import pickle

class Shape:
    def __init__(self):
        pass
    
    def Show(self):
        pass
    
    def Save(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self, file)
        print(f"Фигура сохранена в файл {filename}")
    
    @staticmethod
    def Load(filename):
        with open(filename, 'rb') as file:
            shape = pickle.load(file)
        return shape

class Square(Shape):
    def __init__(self, x, y, side_length):
        super().__init__()
        self.x = x
        self.y = y
        self.side_length = side_length
    
    def Show(self):
        print(f"Квадрат: Левый верхний угол ({self.x}, {self.y}), Длина стороны: {self.side_length}")

class Rectangle(Shape):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    def Show(self):
        print(f"Прямоугольник: Левый верхний угол ({self.x}, {self.y}), Ширина: {self.width}, Высота: {self.height}")

class Circle(Shape):
    def __init__(self, center_x, center_y, radius):
        super().__init__()
        self.center_x = center_x
        self.center_y = center_y
        self.radius = radius
    
    def Show(self):
        print(f"Окружность: Центр ({self.center_x}, {self.center_y}), Радиус: {self.radius}")

class Ellipse(Shape):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    def Show(self):
        print(f"Эллипс: Левый верхний угол ({self.x}, {self.y}), Ширина описанного прямоугольника: {self.width}, Высота описанного прямоугольника: {self.height}")


shapes = [
    Square(0, 0, 10),
    Rectangle(5, 5, 8, 6),
    Circle(0, 0, 5),
    Ellipse(10, 10, 12, 8)
]

filename = 'shapes_data.pkl'
for shape in shapes:
    shape.Save(filename)

loaded_shapes = []
try:
    with open(filename, 'rb') as file:
        while True:
            try:
                shape = Shape.Load(filename)
                loaded_shapes.append(shape)
            except EOFError:
                break
except FileNotFoundError:
    print(f"Файл {filename} не найден.")

for shape in loaded_shapes:
    shape.Show()
