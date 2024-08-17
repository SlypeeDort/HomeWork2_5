def get_matrix():
    columns = int(input('Введите количество столбцов '))
    lines = int(input('Введите количество строк '))
    value = int(input('Введите число '))
    matrix = []
    for i in range(lines):
        list = []
        matrix.append(list)
        for j in range(columns):
            list.append(value)
    return matrix


result1 = get_matrix()
result2 = get_matrix()
result3 = get_matrix()
print('1 ' + str(result1))
print('2 ' + str(result2))
print('3 ' + str(result3))
