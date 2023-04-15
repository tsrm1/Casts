def add(*args, **kwargs):       # * - упаковка позиционных аргументов (args) в кортеж, (_, _, _), ** - упаковка именованых аргументов (key word args) в кортеж, (_, _, _)
    print(args)
    print(kwargs)
    s = sum(args)

    return s


list_num = [1, 2, 3, 4]
dict_addr = { 'street': 'Schevchenko', 'house': 2}

print(add(1, 2))
print(add(1, 2, 3))
print(add(*list_num))


print()
print(add(1, 2, street='Schevchenko'))
print(add(*list_num, street='Schevchenko', hause=2))
print(add(*list_num, **dict_addr))      # * - распаковка списка в кортеж, (_, _, _), ** - распаковка словаря в кортеж, (_, _, _)