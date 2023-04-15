X = 6

# с использованием else
for i in range(5):
    if i == X:
        print(i)
        break
else:                               # срабатывает при нормальном завершении цикла, если break не сработал
    print('X not Found')




# без использования else
flag = True
for i in range(5):
    if i == X:
        print(i)
        flag = False
        break

if flag:
    print('X not Found')