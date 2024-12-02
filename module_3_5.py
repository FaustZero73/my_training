def get_multiplied_digits(number):
    str_number = str(number)
    if str_number.endswith('0'):  # убирать нули
        str_number = str_number[:len(str_number) - 1]
    if len(str_number) > 1:
        first = int(str_number[0])
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return int(str_number)


result = get_multiplied_digits(40203)
print(result)

result2 = get_multiplied_digits(402030)
print(result2)