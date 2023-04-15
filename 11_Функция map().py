# map(function, iterable)

def upper(string):
    return string.upper()

list_0 = ['one', 'two', 'three']

# использование функции map() и внешней функции
new_list_1 = list(map(upper, list_0))
print(new_list_1)

# использование map() и анонимных лямбда-функций
new_list_2 = list(map(lambda string: string.upper(), list_0))
print(new_list_2)

# Использование генератора списков list-comprehension
new_list_3 = [string.upper() for string in list_0]
print(new_list_3)