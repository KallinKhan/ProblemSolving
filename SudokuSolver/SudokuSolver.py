def one_number_per_square():
    for row in range(1, 10):
        for column in range(1, 10):
            entry_clause = ''
            for value in range(1, 10):
                entry_clause += "{} ".format(100 * row + 10 * column + value)
            save.write(entry_clause + "0\n")

def once_per_row():
    for row in range(1, 10):
        for value in range(1, 10):
            for col_one in range(1, 10):
                for col_two in range(col_one + 1, 10):
                    save.write("-{} -{} 0\n".format(100 * row + 10 * col_one + value, 100 * row + 10 * col_two + value))

def once_per_column():
    for column in range(1, 10):
        for value in range(1, 10):
            for row_one in range(1, 10):
                for row_two in range(row_one + 1, 10):
                    save.write("-{} -{} 0\n".format(100 * row_one + 10 * column + value, 100 * row_two + 10 * column + value))

def once_per_subgrid():
    for subrow in range(0, 9, 3):
        for subcolumn in range(0, 9, 3):
            for value in range(1, 10):
                for row in range(1, 4):
                    for col_one in range(1, 4):
                        for col_two in range(col_one + 1, 4):
                            save.write("-{} -{} 0\n".format(100 * (row + subrow) + 10 * (col_one + subcolumn) + value,
                                                            100 * (row + subrow) + 10 * (col_two + subcolumn) + value))

def table_initialization(file):
    start_clause = ''
    for row, line in enumerate(file, start=1):
        column = 1
        for element in line:
            if element != '0':
                start_clause += "{} ".format(100 * row + 10 * column + int(element))
                save.write(start_clause + "0\n")
                start_clause = ''
            column += 1

def sudoku_solve(file):
    table_initialization(file)
    one_number_per_square()
    once_per_row()
    once_per_column()
    once_per_subgrid()

with open('C:\\text_files\\sudoku1.txt', 'r') as before:
    file = [line.strip().replace(' ', '') for line in before]

save = open('C:\\text_files\\sudoku1.cnf', 'w')
save.write("p cnf 999 999999\n")
sudoku_solve(file)
save.close()
