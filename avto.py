# Класс колеса
class Wheels:
    def __init__(self, count, type):
        self.count = count  
        self.type = type    
    
    def display_info(self):
        print(f"Количество колес: {self.count}")
        print(f"Тип колес: {self.type}")

class Engine:
    def __init__(self, type, power):
        self.type = type    
        self.power = power  
    
    def display_info(self):
        print(f"Тип двигателя: {self.type}")
        print(f"Мощность двигателя: {self.power} л.с.")

class Doors:
    def __init__(self, count, specification):
        self.count = count              
        self.specification = specification  
    
    def display_info(self):
        print(f"Количество дверей: {self.count}")
        print(f"Спецификация дверей: {self.specification}")

class Car(Wheels, Engine, Doors):
    def __init__(self, brand, model, wheels_count, wheels_type, engine_type, engine_power, doors_count, doors_spec):
        Wheels.__init__(self, wheels_count, wheels_type)
        Engine.__init__(self, engine_type, engine_power)
        Doors.__init__(self, doors_count, doors_spec)
        
        self.brand = brand    
        self.model = model    
    
    def display_info(self):
        print(f"Марка: {self.brand}")
        print(f"Модель: {self.model}")
        super().display_info()  

def main():
    car = Car("Toyota", "Camry", 4, "summer", "спорт", 200, 4, "бензиновый")
    
    print("Информация о автомобиле:")
    car.display_info()

if __name__ == "__main__":
    main()
