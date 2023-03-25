import os

import reformatter
import duplicate_removal
import shuffler

def menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Добро пожаловать в программу для работы с файлами')
    choice_filename = input('Введите имя файла: ')
    print('''
    Выберите действие:
    1. Перезаписать данные
    2. Удалить дубликаты
    3. Перемешать данные
    4. Выход
    ''')
    choice = input('Введите номер: ')
    if choice == '1':
        reformatter.reformatter(choice_filename)
    elif choice == '2':
        duplicate_removal.duplicate_removal(choice_filename)
    elif choice == '3':
        shuffler.shuffler(choice_filename)
    elif choice == '4':
        exit()
    else:
        print('Неверный ввод')
        menu()

if __name__ == '__main__':
    menu()
