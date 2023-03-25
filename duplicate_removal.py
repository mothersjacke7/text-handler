def  duplicate_removal (filename): 
    with open(filename, 'r') as f:
        lines = f.readlines()
    unique_lines = set()
    duplicate_lines = set()
    for line in lines:
        if line in unique_lines:
            duplicate_lines.add(line)
        else:
            unique_lines.add(line)
    with open('result.txt', 'w') as f:
        for line in lines:
            if line not in duplicate_lines:
                f.write(line)
    print(f'Файл {filename} перезаписан в файл result.txt')