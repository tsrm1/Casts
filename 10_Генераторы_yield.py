def countdown(n):                   # управление передаёся только после выполнения всего цикла
    result = []
    while n != 0:
        result.append(n-1)
        n -= 1
    return result

print('Создание списка с помощью цикла', countdown(4))



def gen_countdown(n):               # управление передаёся после выполнения каждой итерации цикла
    while n != 0:
        yield n - 1
        n -= 1

g = gen_countdown(4)
print(next(g))
print(next(g))
print(next(g))
print(next(g))

print()

for i in gen_countdown(4):
    print(i)