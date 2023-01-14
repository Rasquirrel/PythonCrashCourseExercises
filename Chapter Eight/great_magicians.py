magicians = ['pablo', 'tim', 'franchesco']


def make_great(magicians_list: list):
    length = len(magicians_list)
    for number in range(length):
        magicians_list[number] = 'the Great ' + magicians_list[number].title()


def show_magicians(magicians_list: list):
    for magician in magicians_list:
        print(magician.title())


make_great(magicians)
show_magicians(magicians)
