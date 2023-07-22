# w - write: yozish 
# r - read: o'qish
# a - append: qo'shish

# file = open(file = "birinchi_file.txt", mode = "w")     # создание файла
# file.write("Yangi text yozdim")                         # .write - помогает писать в файле
# file.close()                                            # .close() - закрывает файл

# file = open(file = "birinchi_file.txt", mode = "a")
# file.write("\nHello, World!")
# file.close()      

# file = open(file = "birinchi_file.txt", mode = "r")
# print(file.read())                                      # .read - выводит текст файла в консоль

file = open(file = "birinchi_file.txt", mode = "r")
# print(file.read())
# print(file.readline())
print(file.readlines())

