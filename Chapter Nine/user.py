class User:
    """Attempt to build a user"""
    def __init__(self, first_name, last_name, middle_name='', **user_info):
        """
        Initial method to acquire the attributes:
        first_name: The user's first name
        last_name: The user's last name
        middle_name: Optional. The user's middle name
        **user_info: Optional. You can add how much info about the user
                     as you want. The info will be added to a dictionary
                     called user_info
        """
        self.first_name = first_name
        self.last_name = last_name

        if middle_name:
            self.middle_name = middle_name
            self.full_name = first_name + " " + middle_name + " " + last_name
        else:
            self.full_name = first_name + " " + last_name

        if user_info:
            self.user_info = user_info

    def describe_user(self):
        """Prints all information about the user"""
        print('These are the info about user: ' + self.full_name.title())
        print('\tFirst Name: ' + self.first_name.title())
        print('\tLast Name: ' + self.last_name.title())
        print('\tFull Name: ' + self.full_name.title())

        if self.user_info:
            for key, value in self.user_info.items():
                if type(value) != str:
                    print('\t' + key.title() + ': ' + str(value).title())
                else:
                    print('\t' + key.title() + ': ' + value.title())

    def greet_user(self):
        print('Hello ' + self.full_name.title() + '! Nice to see you again!')
