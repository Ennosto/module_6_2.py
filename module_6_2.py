"""
Вам необходимо создать 2 класса: Vehicle и Sedan, где Vehicle - это любой транспорт,
а Sedan(седан) - наследник класса Vehicle.

I. Каждый объект Vehicle должен содержать следующие атрибуты объекта:

    Атрибут owner(str) - владелец транспорта. (владелец может меняться)
    Атрибут __model(str) - модель (марка) транспорта. (мы не можем менять название модели)
    Атрибут __engine_power(int) - мощность двигателя. (мы не можем менять мощность двигателя самостоятельно)
    Атрибут __color(str) - название цвета. (мы не можем менять цвет автомобиля своими руками)

А так же атрибут класса:

    Атрибут класса __COLOR_VARIANTS, в который записан список допустимых цветов для окрашивания. (Цвета написать свои)


Каждый объект Vehicle должен содержать следующий методы:

    Метод get_model - возвращает строку: "Модель: <название модели транспорта>"
    Метод get_horsepower - возвращает строку: "Мощность двигателя: <мощность>"
    Метод get_color - возвращает строку: "Цвет: <цвет транспорта>"
    Метод print_info - распечатывает результаты методов (в том же порядке): get_model, get_horsepower, get_color;
    а так же владельца в конце в формате "Владелец: <имя>"
    Метод set_color - принимает аргумент new_color(str), меняет цвет __color на new_color,
    если он есть в списке __COLOR_VARIANTS, в противном случае выводит на экран надпись: "Нельзя сменить цвет
    на <новый цвет>".


"""
class Vehicle():
    def __init__(self, owner, __model, __color, __engine_power):
        self.owner = str(owner)
        self.__model = str(__model)
        self.__engine_power = int(__engine_power)
        self.__color = str(__color)
    __COlOR_VARIANT = ['blue', 'red', 'green', 'black', 'white']


    def get_model(self):
        return f'Модель: {self.__model}'


    def get_horsepower(self):
        return f'Мощность двигателя: {self.__engine_power}'



    def get_color(self):
        return f"Цвет: {self.__color}"


    def print_info(self):
        print(f'{Vehicle.get_model(self)}, {Vehicle.get_horsepower(self)}, {Vehicle.get_color(self)}, Владелец: {self.owner}')


    def set_color(self, new_color):
        self.new_color = new_color
        for i in self.__COlOR_VARIANT:
            if i.lower() == self.new_color.lower():
                self.__color = new_color
                break
        else:
            print(f"Нельзя сменить цвет на {self.new_color}")





class Sedan(Vehicle):
    __PASSANGERES_LIMIT = 5




# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
