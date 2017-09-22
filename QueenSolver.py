def oneInEveryRow(n):
    row_string = ''
    for i in range(1, n * n + 1):
        row_string += str(i) + ' '
        if i % n == 0:
            file.write(row_string + '0\n')
            row_string = ''


def handleColumns(j, n):
    for i in range(1, (j - 1) // n + 1):
        file.write('-%s -%s 0\n' % (j - n * i,j ))  # column


def handleRows(j, n):
    for i in range(1, n - (n * n - j) % n):
        file.write('-%s -%s 0\n' % (j - i, j))  # row


def handleDiags(j, n):
    right_wall = False
    left_wall = False
    for i in range(1, (j - 1) // n + 1):
        if j % n == 0:
            file.write('-%s -%s 0\n' % (j - (n + 1) * i, j))
        elif j % n == 1:
            file.write('-%s -%s 0\n' % (j - (n - 1) * i, j))
        else:
            if not right_wall:
                file.write('-%s -%s 0\n' % (j - (n - 1) * i, j))
                if (j - (n - 1) * i) % n == 0:
                    right_wall = True
            if not left_wall:
                file.write('-%s -%s 0\n' % (j - (n + 1) * i, j))
                if (j - (n + 1) * i - 1) % n == 0:
                    left_wall = True


def createCNFforNQueens(n):
    oneInEveryRow(n)
    for i in range(n * n, 1, -1):
        handleColumns(i, n)
    for i in range(n * n, 1, -1):
        handleRows(i, n)
    for i in range(n * n, 1, -1):
        handleDiags(i, n)

num_queens = 100
file = open("C:\\text_files\\queen" +str(num_queens)+'.cnf', 'w')
createCNFforNQueens(num_queens)
file.close()