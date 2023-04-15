user1 = {
    'name': 'jack',
    'car': 'bmw'
}

user2 = {
    'name': 'john',
    'car': 'audi'
}

user3 = {
    'name': 'valerie',
}

users = [user1, user2]  # список словарей, пользователей

print('user1 = ', user1)
print('user2 = ', user2)
print('users = ', users)

# использование цикла for в обычном виде (3 строки)
cars = []
for person in users:
    cars.append(person['car'])

print('cars = ', cars)

# использование генератора списка list comprehension (1 строка). Работает быстрее !!!
cars = [person['car'] for person in users] 

print('cars = ', cars)

# использование генератора списка list comprehension (1 строка) c обработкой исключения (при отсутствии ключа в словаре)
users = [user1, user2, user3]  # список словарей, пользователей. У user3 нет ключа 'car'
cars = [person.get('car', '') for person in users] 

print('cars = ', cars)


names = ['Jack', 'john', 'oleg', 'Julia']

# создание нового списка из элементов, удовлетворяющих условию. использование цикла for в обычном виде (4 строки)
new_names = []
for n in names:
    if n.lower().startswith('j'):
        new_names.append(n)

print(new_names)

# создание нового списка из элементов, удовлетворяющих условию. Использование list comprehension (1 строка)
new_names = [n for n in names if n.lower().startswith('j')]

print(new_names)