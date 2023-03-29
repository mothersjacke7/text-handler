import os

def intersections(filename):
    file1 = filename
    print('Первый файл с которым будем сравнивать:' + file1)
    path1 = os.path.join(os.getcwd(), file1)

    file2 = input("Введите имя второго файла: ")
    path2 = os.path.join(os.getcwd(), file2)

    output_file = "output.txt"
    output_path = os.path.join(os.getcwd(), output_file)

    with open(path1, "r") as f1:
        file1_lines = f1.readlines()

    with open(path2, "r") as f2:
        file2_lines = f2.readlines()

    matching_lines = [line for line in file1_lines if line in file2_lines]

    with open(output_path, "w") as output:
        output.writelines(matching_lines)
    print(f'Файл {filename} перезаписан в файл result.txt')
