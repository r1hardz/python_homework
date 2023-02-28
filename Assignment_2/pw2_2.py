ver_bar = "|"
asterisk_symbol = "*"

def draw_spaces(spaceCount):
    space = ""
    for i in range(spaceCount):
       space += " "

    return space

def draw_dashes():
    dash = "-"

    print()
    for i in range(22):
        print(dash, end="")

def draw_circle():

    star_count = 8
    space_count = 6


    for i in range(5):
        print()

        if i == 4:
            star_count = 12
            space_count = 4

        if i == 0 or i == 1:

            draw_line(space_count, star_count, ver_bar, asterisk_symbol)

            space_count -= 2
            star_count += 4

        elif i == 2 or i == 3:
            star_count = 4
            space_count = 2

            draw_middle_line(space_count, star_count, ver_bar, asterisk_symbol)
        else:

            draw_line(space_count, star_count, ver_bar, asterisk_symbol)

            space_count += 1
            star_count -= 2

#function that prints a single line based on params
def draw_line(spaces, stars, bars, asterisks):
    print(bars, end="")
    print(draw_spaces(spaces), end="")

    for j in range(stars):
        print(asterisks, end="")

    print(draw_spaces(spaces), end="")
    print(bars, end="")

def draw_middle_line(spaces, stars, bars, asterisks):
    print(bars, end="")
    print(draw_spaces(spaces), end="")

    for j in range(stars):
        print(asterisks, end="")

    print(draw_spaces(spaces + 6), end="")

    for j in range(stars):
        print(asterisks, end="")

    print(draw_spaces(spaces), end="")

    print(bars, end="")


def draw_last_line():

    star_count = 8
    space_count = 6

    print()

    draw_line(space_count, star_count, ver_bar, asterisk_symbol)



if __name__ == '__main__':

    draw_dashes()

    draw_circle()
    draw_circle()
    draw_last_line()

    draw_dashes()
