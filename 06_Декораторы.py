from time import time 

n = 7

def generate_list_1(n):
    print('Run generate_list_1')
    t0 = time()
    list_1 = []
    for i in range(n):
        if i % 2 == 0:
            list_1.append(i)
    t1 = time()
    print('v1 elapsed ', t1 - t0, 'seconds')
    print()
    return t1 - t0

def generate_list_2(n):
    print('Run generate_list_2')
    t2 = time()
    list_2 = [i for i in range(n) if i % 2 == 0]
    t3 = time()
    print('v2 elapsed ', t3 - t2, 'seconds')
    print()
    return t3 - t2


print('Generate list from range ', 10 ** n)
dt1 = generate_list_1(10 ** n)
dt2 = generate_list_2(10 ** n)
print('v2 faster, ', round((dt1 - dt2) * 100 / dt2, 1), ' %')
print()

#######################################################################################################

# Декораторы
def timeit(func):
    def wrapper(*args, **kwargs):
        print('Function ',func, 'is started')                                       # дополнительные надстройки
        start = time()                                                              # дополнительные надстройки    
        result = func(*args, **kwargs)                                              # вызов основной функции
        print('Function ',func, 'was ended. It taked ', time() - start, 'seconds')  # дополнительные надстройки   
        return result                                                               # возврат результата основной функции
    return wrapper                                                                  # возврат результата функции обложки

@timeit                         # декоратор =>   = timeit(gen_list)(n) =>  = wrapper(n)
def gen_list_1(arg):
    list_1 = []
    for i in range(10**arg):
        if i % 2 == 0:
            list_1.append(i)
    return list_1

@timeit
def gen_list_2(arg):
    list_2 = [i for i in range(10**arg) if i % 2 == 0]
    return list_2

gen_list_1(n)
gen_list_2(n)

#######################################################################################################

# Декораторы с аргументом

def timeit(arg):
    print(arg)
    def outer(func):                                                                    # вызов внещней обложки
        def wrapper(*args, **kwargs):                                                   # вызов внутренней обложки
            print('Function ',func, 'is started')                                       # дополнительные надстройки
            start = time()                                                              # дополнительные надстройки    
            result = func(*args, **kwargs)                                              # вызов основной функции
            print('Function ',func, 'was ended. It taked ', time() - start, 'seconds')  # дополнительные надстройки   
            return result                                                               # возврат результата основной функции
        return wrapper                                                                  # возврат результата функции внутренней обложки
    return outer                                                                        # возврат результата функции внешней обложки

@timeit('name')                         # декоратор =>   = timeit(gen_list)(n) =>  = wrapper(n)
def gen_1(arg):
    list_1 = []
    for i in range(10**arg):
        if i % 2 == 0:
            list_1.append(i)
    return list_1

@timeit('name')
def gen_2(arg):
    list_2 = [i for i in range(10**arg) if i % 2 == 0]
    return list_2

l1 = timeit('name')(gen_1)(n)
l2 = timeit('name')(gen_2)(n)
