magicians = ['pablo', 'tim', 'franchesco']


def make_great(magicians_list: list):
    length = len(magicians_list)
    for number in range(length):
        magicians_list[number] = 'the Great ' + magicians_list[number].title()
    return magicians_list


def show_magicians(magicians_list: list):
    for magician in magicians_list:
        print(magician.title())


magicians_copy = make_great(magicians[:])
show_magicians(magicians)
show_magicians(magicians_copy)
