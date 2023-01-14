def get_formatted_name(first, last, middle=''):
    """ Returns a full name neatly formatted.
        Names with middle name, should insert
        it as the third argument.
     """
    if middle:
        full_name = first + " " + middle + " " + last
    else:
        full_name = first + " " + last

    return full_name.title()


musician = get_formatted_name('Jimi', 'Hendrix')
print(musician)

girl = get_formatted_name('emilly', 'nascimento', 'do')
print(girl)
