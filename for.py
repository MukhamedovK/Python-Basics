# for i in range(10):
#     print(i)

# for item in range(0, 10):
#     print(item)

# boys = ['Abdullox', 'Sarvar', 'Axmad']

# for name in boys:
#     print(f'Ismi: {name}')

# for i in range(0, 11, 2):
#     print(i)

name = []

while True:
    user = input('Введите что-то:')

    if user != 'stop':
        name.append(user)
    else:
        print(name)
        break

