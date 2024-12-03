# Задача "Магические здания":
class House:
    def __init__(self, name, number_of_floors):
        self.name = name  # имя,
        self.number_of_floors = number_of_floors  # кол - во этажей
    def __len__(self): #- должен возвращать кол-во этажей здания self.number_of_floors.
        return self.number_of_floors
    def __str__(self): #- должен возвращать строку: "Название: <название>, кол-во этажей: <этажи>".
        name_gk = str(f'Название: {self.name}, кол-во этажей: {self.number_of_floors}')
        return name_gk


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)
print(len(h1))
print(len(h2))