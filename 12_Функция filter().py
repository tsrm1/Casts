# filter(function, iterable)

def has_o(string):
    return 'o' in string.lower()

list_0 = ['one', 'two', 'three', 'dsadas']

# использование функции filter() и внешней функции
new_list_1 = list(filter(has_o, list_0))
print(new_list_1)

# использование filter() и анонимных лямбда-функций
new_list_2 = list(filter(lambda string: 'o' in string.lower(), list_0))
print(new_list_2)

# Использование генератора списков list-comprehension
new_list_3 = [string for string in list_0 if 'o' in string.lower()]
print(new_list_3)