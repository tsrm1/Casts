# try:
#     pass
# except:
#     pass
# else:                 # выполняется, если не возникло исключение
#     pass
# finally:              # выполняеться в любом случае
#     pass

def calculate_salt(mass):
    # 1000 : 10 = mass : x
    try:
        mass = int(mass)
    except ValueError as e:
        print(e) 
        mass = 0
    except TypeError as e:
        pass
    except FileNotFoundError as e:
        pass
    except Exception as e:
        pass
    return 10 * mass / 1000

print(calculate_salt('asdf'))