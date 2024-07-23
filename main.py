
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


field = [
    ['1', '*', '2', '1'],
    ['1', '2', '*', '1'],
    ['0', '1', '1', '1'],
    ['0', '0', '0', '0']
    ]

draw_field(field)
