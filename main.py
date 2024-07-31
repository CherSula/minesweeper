import random


def draw_field(field):
    devider_line = "  " + "+---" * len(field[0]) + "+"
    column_numbers = generate_column_numbers(field)
    print(column_numbers)
    print(devider_line)
    for i, row in enumerate(field):
        line = create_line(row, i)
        print(line)
        print(devider_line)


def generate_column_numbers(field):
    column_numbers = "    " + '   '.join(
        [
            str(i + 1)
            for i
            in range(len(field[0]))
        ]
    )
    return column_numbers


def create_line(row, index):
    line = f'{index + 1} |'
    for el in row:
        line += f' {el} |'
    return line


def generate_field_hint_view(field):
    data_view = generate_empty_field(len(field), len(field[0]))
    for row_ind in range(len(field)):
        for col_ind in range(len(field[row_ind])):
            data_view[row_ind][col_ind] = generate_view_for_cell(
                field, row_ind, col_ind)
    return data_view


def generate_empty_field(height, width, placeholder=''):
    empty_field = []
    for _ in range(height):
        el = []
        empty_field.append(el)
        for _ in range(width):
            el.append(placeholder)
    return empty_field


def generate_view_for_cell(field, r_ind, c_ind):
    value = field[r_ind][c_ind]
    if value == 1:
        return '*'

    counter = 0
    left_col_index = c_ind - 1
    right_col_index = c_ind + 1
    up_row_index = r_ind - 1
    down_row_index = r_ind + 1

    if left_col_index >= 0 and field[r_ind][left_col_index] == 1:
        counter += 1
    if (
        right_col_index < len(field[r_ind])
        and field[r_ind][right_col_index] == 1
    ):
        counter += 1
    if (
        left_col_index >= 0
        and down_row_index < len(field)
        and field[down_row_index][left_col_index] == 1
    ):
        counter += 1

    if down_row_index < len(field) and field[down_row_index][c_ind] == 1:
        counter += 1
    if (
        down_row_index < len(field)
        and right_col_index < len(field[r_ind])
        and field[down_row_index][right_col_index] == 1
    ):
        counter += 1

    if (
        left_col_index >= 0
        and up_row_index >= 0
        and field[up_row_index][left_col_index] == 1
    ):
        counter += 1

    if (
        up_row_index >= 0
        and field[up_row_index][c_ind] == 1
    ):
        counter += 1
    if (
        up_row_index >= 0
        and right_col_index < len(field[r_ind])
        and field[up_row_index][right_col_index] == 1
    ):
        counter += 1

    return str(counter)


def open_cell(mask_field, r_index, c_index, field_hint_view):
    mask_field[r_index][c_index] = field_hint_view[r_index][c_index]


def ask_cell():
    row_index = int(input('Введите номер строки открываемой ячейки: ')) - 1
    column_index = int(input('Введите номер столбца открываемой ячейки: ')) - 1
    return row_index, column_index


def setup_bombs(field, bombs):
    height = len(field)
    width = len(field[0])
    while bombs > 0:
        ir = random.randint(0, height-1)
        ic = random.randint(0, width-1)
        if field[ir][ic] != 1:
            field[ir][ic] = 1
            bombs -= 1


bombs_in_game = 2
height = 3
width = 4
field = generate_empty_field(height, width, 0)  # type: ignore
setup_bombs(field, bombs_in_game)
safe_cells = len(field) * len(field[0]) - bombs_in_game
field_hint_view = generate_field_hint_view(field)
mask_field = generate_empty_field(height, width, '?')
draw_field(mask_field)

while True:
    # считывание ввода пользователя
    row_index, column_index = ask_cell()
    # реакция на ввод пользователя
    if row_index > len(field) or row_index < 0:
        print('Вы ввели неверное число для строки')
        continue
    if column_index > len(field[0]) or column_index < 0:
        print('Вы ввели неверное число для столбца')
        continue
    if field[row_index][column_index]:
        print('-----------------------------')
        print('Вы попали на бомбу! GAME OVER')
        print('-----------------------------')
        draw_field(field_hint_view)
        break
    # изменение состояния игры
    open_cell(mask_field, row_index, column_index, field_hint_view)

    # перерисовка игры
    draw_field(mask_field)

    safe_cells -= 1
    if safe_cells == 0:
        print('------------------------------')
        print('Вы прошли минное поле! YOU WIN')
        print('------------------------------')
        break
