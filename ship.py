class Ship:
    def __init__(self, name, length, max_speed):
        self.name = name
        self.length = length  
        self.max_speed = max_speed  
    
    def set_name(self, name):
        self.name = name
    
    def set_length(self, length):
        self.length = length
    
    def set_max_speed(self, max_speed):
        self.max_speed = max_speed
    
    def get_name(self):
        return self.name
    
    def get_length(self):
        return self.length
    
    def get_max_speed(self):
        return self.max_speed
    
    def display_info(self):
        print(f"Название: {self.name}")
        print(f"Длина: {self.length} м")
        print(f"Максимальная скорость: {self.max_speed} узлов")


class Frigate(Ship):
    def __init__(self, name, length, max_speed, missile_count):
        super().__init__(name, length, max_speed)
        self.missile_count = missile_count 
    
    def set_missile_count(self, missile_count):
        self.missile_count = missile_count
    
    def get_missile_count(self):
        return self.missile_count
    
    def fire_missile(self):
        print(f"{self.name} выпустил ракету!")

class Destroyer(Ship):
    def __init__(self, name, length, max_speed, gun_caliber):
        super().__init__(name, length, max_speed)
        self.gun_caliber = gun_caliber  
    
    def set_gun_caliber(self, gun_caliber):
        self.gun_caliber = gun_caliber
    
    def get_gun_caliber(self):
        return self.gun_caliber
    
    def fire_gun(self):
        print(f"{self.name} открыл огонь с артиллерии!")

class Cruiser(Ship):
    def __init__(self, name, length, max_speed, aircraft_count):
        super().__init__(name, length, max_speed)
        self.aircraft_count = aircraft_count  
    
    def set_aircraft_count(self, aircraft_count):
        self.aircraft_count = aircraft_count
    
    def get_aircraft_count(self):
        return self.aircraft_count
    
    def launch_aircraft(self):
        print(f"{self.name} запустил самолеты!")


def main():
    frigate = Frigate("Frigate A", 120, 35, 40)
    destroyer = Destroyer("Destroyer B", 150, 40, 130)
    cruiser = Cruiser("Cruiser C", 180, 30, 20)

    print("Информация о фрегате:")
    frigate.display_info()
    print(f"Количество ракет: {frigate.get_missile_count()}")
    frigate.fire_missile()
    print()

    print("Информация об эсминце:")
    destroyer.display_info()
    print(f"Калибр артиллерии: {destroyer.get_gun_caliber()} мм")
    destroyer.fire_gun()
    print()

    print("Информация о крейсере:")
    cruiser.display_info()
    print(f"Количество самолетов: {cruiser.get_aircraft_count()}")
    cruiser.launch_aircraft()

if __name__ == "__main__":
    main()
