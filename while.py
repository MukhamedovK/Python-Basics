# i = 0
# while i <= 10:
#     print(i)
#     i += 1

# my_list = ["Nola", "Lola", "Gul", "Atirgul"]

# i = 0
# while i < len(my_list):
#     if my_list[i] != "Lola":
#         print(my_list[i])
#     i += 1

    
# new_list = ['Nexia', 'Gentra', 'Damas', 'Tico', 'Matiz', 'Cobalt']

# k = 0

# while k < len(new_list):
#     print(new_list[k])
#     k += 1
#     if new_list[k] == "Tico":
#         break

# while k < len(new_list):
#     if new_list[k] == "Tico":
#         k += 1
#         continue
#     print(new_list[k])
#     k += 1


import random

new_num = random.randint(1, 100)

words = {
    'win': '🥳 Tabriklaymiz siz g`olib bo`ldingiz!',
    'lose': '😕 Siz topaolmadingiz. Yana urinib ko`ring!'
}

while True:
    user_num = int(input('Найдите число (от 1 до 10):'))

    if user_num == new_num:
        print(words['win'])
        break

    print(words['lose'])