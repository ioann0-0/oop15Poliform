class Device:
    def __init__(self, brand, model, power):
        self.brand = brand
        self.model = model
        self.power = power
    
    def set_brand(self, brand):
        self.brand = brand
    
    def set_model(self, model):
        self.model = model
    
    def set_power(self, power):
        self.power = power
    
    def get_brand(self):
        return self.brand
    
    def get_model(self):
        return self.model
    
    def get_power(self):
        return self.power
    
    def display_info(self):
        print(f"Бренд: {self.brand}")
        print(f"Модель: {self.model}")
        print(f"Мощность: {self.power} Вт")

class CoffeeMachine(Device):
    def __init__(self, brand, model, power, cups):
        super().__init__(brand, model, power)
        self.cups = cups  
    
    def set_cups(self, cups):
        self.cups = cups
    
    def get_cups(self):
        return self.cups
    
    def brew_coffee(self):
        print(f"{self.brand} {self.model} готовит кофе!")

class Blender(Device):
    def __init__(self, brand, model, power, speeds):
        super().__init__(brand, model, power)
        self.speeds = speeds  
    
    def set_speeds(self, speeds):
        self.speeds = speeds
    
    def get_speeds(self):
        return self.speeds
    
    def blend(self):
        print(f"{self.brand} {self.model} включен на максимальной скорости!")

class MeatGrinder(Device):
    def __init__(self, brand, model, power, capacity):
        super().__init__(brand, model, power)
        self.capacity = capacity  
    
    def set_capacity(self, capacity):
        self.capacity = capacity
    
    def get_capacity(self):
        return self.capacity
    
    def grind_meat(self):
        print(f"{self.brand} {self.model} начал молоть мясо!")

def main():
    coffee_machine = CoffeeMachine("Breville", "BES870XL", 1600, 2)
    blender = Blender("Vitamix", "5200", 1400, 10)
    meat_grinder = MeatGrinder("KitchenAid", "FGA", 250, 500)

    print("Информация о кофемашине:")
    coffee_machine.display_info()
    print(f"Может приготовить {coffee_machine.get_cups()} чашек за раз.")
    coffee_machine.brew_coffee()
    print()

    print("Информация о блендере:")
    blender.display_info()
    print(f"Количество скоростей: {blender.get_speeds()}")
    blender.blend()
    print()

    print("Информация о мясорубке:")
    meat_grinder.display_info()
    print(f"Вместимость мясорубки: {meat_grinder.get_capacity()} г")
    meat_grinder.grind_meat()

if __name__ == "__main__":
    main()
