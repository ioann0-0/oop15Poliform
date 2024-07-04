class Stadium:
    def init(self, name):
        self.__name = name  
        self.__opening_date = ""
        self.__country = ""
        self.__city = ""
        self.__capacity = 0
    
    def input_data(self):
        self.__name = input("Введите название стадиона: ")
        self.__opening_date = input("Введите дату открытия стадиона: ")
        self.__country = input("Введите страну: ")
        self.__city = input("Введите город: ")
        self.__capacity = int(input("Введите вместимость стадиона: "))

    def display_data(self):
        print(f"Название стадиона: {self.__name}")
        print(f"Дата открытия: {self.__opening_date}")
        print(f"Страна: {self.__country}")
        print(f"Город: {self.__city}")
        print(f"Вместимость: {self.__capacity}")

    def get_name(self):
        return self.__name

    def get_opening_date(self):
        return self.__opening_date

    def get_country(self):
        return self.__country

    def get_city(self):
        return self.__city

    def get_capacity(self):
        return self.__capacity

    def set_name(self, name):
        self.__name = name

    def set_opening_date(self, opening_date):
        self.__opening_date = opening_date

    def set_country(self, country):
        self.__country = country

    def set_city(self, city):
        self.__city = city

    def set_capacity(self, capacity):
        self.__capacity = capacity


class ExtendedStadium(Stadium):
    def init(self, name, matches_played):
        super().init(name)
        self.matches_played = matches_played  
    
    def get_matches_played(self):
        return self.matches_played
    
    def set_matches_played(self, matches_played):
        self.matches_played = matches_played
    
    def display_data(self):
        super().display_data()
        print(f"Количество матчей: {self.matches_played}")


def main():
    stadium1 = ExtendedStadium("Stadium ABC", 50)
    stadium1.input_data()

    print("\nДанные о стадионе:")
    stadium1.display_data()

    print("\nНазвание стадиона:", stadium1.get_name())
    print("Дата открытия:", stadium1.get_opening_date())
    print("Страна:", stadium1.get_country())
    print("Город:", stadium1.get_city())
    print("Вместимость:", stadium1.get_capacity())
    print("Количество матчей:", stadium1.get_matches_played())

if __name__ == "main":
    main()