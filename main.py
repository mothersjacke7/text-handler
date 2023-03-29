import os

from modules import reformatter, duplicate_removal, shuffler, txtinone, separator, intersections

def menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Добро пожаловать в программу для работы с файлами.')
    choice_filename = input('Введите имя файла: ')
    print('''
    Выберите действие:
    1. Перезаписать данные ("1:2:3..." -> "1:2")
    2. Удалить дубликаты
    3. Перемешать данные
    4. Соединить все файлы в один
    5. Разделить файл на несколько файлов (по размеру)
    6. Сравнить 2 файла и записать совпадения в отдельный.
    0. Выход

    https://github.com/mothersjacke7
    ''')
    choice = input('Введите номер: ')
    if choice == '1':
        reformatter.reformatter(choice_filename)
        menu()
    elif choice == '2':
        duplicate_removal.duplicate_removal(choice_filename)
        menu()
    elif choice == '3':
        shuffler.shuffler(choice_filename)
        menu()
    elif choice == '4':
        txtinone.txtinone(choice_filename)
        menu()
    elif choice == '5':
        separator.split_file(choice_filename)
        menu()
    elif choice == '6':
        intersections.intersections(choice_filename)
        menu()
    elif choice == '0':
        exit()
    else:
        print('Неверный ввод')
        menu()

if __name__ == '__main__':
    menu()
