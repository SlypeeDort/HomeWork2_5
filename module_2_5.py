def get_matrix(columns, lines, value):
    matrix = []
    for i in range(lines):
        list = []
        matrix.append(list)
        for j in range(columns):
            list.append(value)
    return matrix


result1 = get_matrix(int(input('Введите количество столбцов ')),
                     int(input('Введите количество строк ')),
                     int(input('Введите число ')))
print('1 ' + str(result1))
