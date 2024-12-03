# Задача "Нужно больше этажей":
class House:
    def __init__(self, name, number_of_floors):
        self.name = name  # имя,
        self.number_of_floors = number_of_floors  # кол - во этажей
    def __len__(self): #- должен возвращать кол-во этажей здания self.number_of_floors.
        return self.number_of_floors
    def __str__(self): #- должен возвращать строку: "Название: <название>, кол-во этажей: <этажи>".
        name_gk = str(f'Название: {self.name}, кол-во этажей: {self.number_of_floors}')
        return name_gk

    def __eq__(self, other): #должен возвращать True, если количество этажей одинаковое у self и у other
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors == other.number_of_floors

    def __lt__(self, other): #должны присутствовать в классе и возвращать результаты сравнения по соответствующим операторам
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors != other.number_of_floors

    def __add__(self, value): #увеличивает кол-во этажей на переданное значение value, возвращает сам объект self
        if isinstance(value, int):
            self.number_of_floors = self.number_of_floors + value
        return self

    def __radd__(self, value): #работают так же как и __add__ (возвращают результат его вызова).
        return self.__add__(value)

    def __iadd__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
        return self

#Остальные методы арифметических операторов, где self - x, other - y:


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)
print(h1 == h2) # __eq__
h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)
h1 += 10 # __iadd__
print(h1)
h2 = 10 + h2 # __radd__
print(h2)
print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__

