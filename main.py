
def draw_field(field):
    devider_line = "+---" * len(field[0]) + "+"
    print(devider_line)
    for row in field:
        line = create_line(row)
        print(line)
        print(devider_line)


def create_line(row):
    line = '|'
    for el in row:
        line += f' {el} |'
    return line


def generate_field_hint_view(field):
    data_view = generate_empty_field(field)
    for row_ind in range(len(field)):
        for col_ind in range(len(field[row_ind])):
            data_view[row_ind][col_ind] = generate_view_for_cell(
                field, row_ind, col_ind)
    return data_view


def generate_empty_field(field, placeholder=''):
    height = len(field)
    width = len(field[0])
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


field = [
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
    ]

field_hint_view = generate_field_hint_view(field)
mask_field = generate_empty_field(field, '?')
draw_field(mask_field)
