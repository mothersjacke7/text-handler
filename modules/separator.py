import os

def split_file(filename):
    if not os.path.isfile(filename):
        print(f"Ошибка: файл '{filename}' не существует.")
        return
    filename_base, filename_ext = os.path.splitext(filename)
    dir_name = f"{filename_base}_parts"
    os.makedirs(dir_name, exist_ok=True)

    while True:
        max_size = input('Введите максимальный размер файла в байтах: ')
        if max_size.isnumeric():
            print('Разделение файла на части...')
            max_size = int(max_size)
            break
        else:
            print("Ошибка: введите целое число.")

    with open(filename, 'r') as f:
        chunk = f.read(max_size)
        index = 0

        while chunk:
            new_file_name = f"{filename_base}_{index}{filename_ext}"
            new_file_path = os.path.join(dir_name, new_file_name)
            with open(new_file_path, 'w') as new_file:
                new_file.write(chunk)
            chunk = f.read(max_size)
            index += 1
print('Разделение файла на части завершено.')