# def myFunction(x):
#     print(x,  2)


# myFunction(4)
# myFunction(6)
# myFunction(8)

# print(4,  2)
# print(8,  2)
# print(42,  2)
# print(420 ** 2)

# def hide_cart_number(cart_number):
#     result = ''
#     if len(cart_number) == 16:
#         for index, i in enumerate(cart_number):
#             if index > 3:
#                 result += '*'
#                 continue
#             result += i
        
#         print(result)
            

# hide_cart_number(input("Karta raqamini kiriting: "))


# def myCard(*args):
#     print(args)
#     new_list = []
#     for i in args:
#         new_list.append(i)

#     print(new_list)
# myCard(1, 8, 2, 85, 'Kamoliddin', 'Abdullox')

# def myData(**kwargs):
#     print(kwargs)

# myData(name = 'Khurshida', in_lesson = 'Yomon', have_laptop = True)

# def func(*args, **kwargs):
#     print(args)
#     print(kwargs)

# func('word', 55, 50.5, word = "word")

def myData(name: str):
    context = f"Assalomu alekum {name}"

    return context

result = myData(input('Ism kiriting: '))
print(result)