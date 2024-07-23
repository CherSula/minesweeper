
def generate_field(width, height):
    devider_line = "+---" * width + "+"
    for _ in range(1, height+1):
        print(devider_line)
        first_line = ("| " + ' ' + " ") * width + "|"
        print(first_line)
    print(devider_line)


generate_field(6, 3)
