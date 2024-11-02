first = int(input('Введите целое число: '))
second = int(input('Введите целое число: '))
third = int(input('Введите целое число: '))
if first == second == third:
    print(3)
elif third != first and third != second and second != third:
    print(0)
else:
    print(2)