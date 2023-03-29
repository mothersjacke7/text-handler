import random

def shuffler (filename):
    with open(filename, 'r') as input_file:
        lines = input_file.readlines()
    random.shuffle(lines)
    with open('result.txt', 'w') as output_file:
        output_file.writelines(lines)
    print(f'Файл {filename} перезаписан в файл result.txt')