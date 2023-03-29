def reformatter(filename):
    with open(filename, 'r') as input_file:
        with open("result.txt", 'w') as output_file:
            for line in input_file:
                split_line = line.split(':')
                output_file.write(split_line[0] + ':' + split_line[1] + '\n')
    print(f'Файл {filename} перезаписан в файл result.txt')
