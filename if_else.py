# if 5 >= 6:
#     print('True')
# else:
#     print('False')

# name = input('Ism:')
# age = int(input('Yosh:'))

# if age > 7:
#     print((name)+' Birbalo')
# elif age == 7:
#     print('Not birbalo')
# else:
#     print('Yes birbalo')

# !, ||, &&
# not, or, and

# a = 2 == 2 or 5 > 9 or 10 == 11
# print(a)


num = int(input('Введите число: '))

if num % 3 == 0:
    print('Python')

if num % 5 == 0:
    print('Asoslari')

if num % 3 == 0 and num % 5 == 0:
    print('Python Asoslari')
else:
    print(num)
