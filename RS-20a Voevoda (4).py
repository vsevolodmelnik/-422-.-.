def transpose(a):
    k = 0
    for i in range(rows):
        a[i] = [int(j) for j in input().strip().split(' ')]
        k+=2
    rows_count = len(a)
    colums_count = len(a[0])
    new_matrix = [[0] * rows_count for _ in range(colums_count)]
    k+=2
    for i in range(rows_count):
        k+=2
        for j in range(colums_count):
            new_matrix[j][i] = a[i][j]
            k+=2
    for row in new_matrix:
        k+=2
        print(*row)
        print('кол-во действий: ',k)


if __name__ == '__main__':
    rows = int(input().strip())
    colums = int(input().strip())
    a = [colums for _ in range(rows)]
    print(transpose(a))
