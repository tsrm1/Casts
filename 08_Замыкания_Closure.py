def one():
    x = ['one', 'two']
    def inner():
        print(x)
        print(id(x))
    return inner

func = one()
print('func =', func)       # ссылка на функцию
print('func() =', func())   # вызов функции

print(func.__closure__[0])
x1 = func.__closure__[0].cell_contents # получаем значение переменной x в области видимости функции
print(x1)    

x1.append('asdf')           # изменяем значение глобальной переменной x1
print('x1.append', x1)      # выводим значение глобальной переменной x1 в консоль
func()                      # значение локальной переменной x тоже изменилось
