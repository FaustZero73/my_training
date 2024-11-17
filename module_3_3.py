#print('1. Функция с параметрами по умолчанию:')

def print_params(a, b, c):
    print(a, b, c)


print_params(a = 1, b = 'строка', c = True)
print_params(a = 1, b = 25, c = [1,2,3])

#print('2.Распаковка параметров:')
def print_params(*args, **kwargs):
    print(*args, kwargs)


values_list = [1, 'строка', True]
values_dict = {'d': 1, 'f': 'строка', 'g': False}
print_params(*values_list, **values_dict)

#print('3.Распаковка + отдельные параметры:')

values_list_2 = [54.32, 'Строка']
#print(values_list_2)

def values_list(item, print_params = None):
    if print_params is None:
        print_params = [*values_list_2, 42]
        print_params.append(item)
    print(print_params)

print_params(*values_list_2, 42)