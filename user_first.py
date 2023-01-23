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


user1 = User(
            'isac',
            'araujo',
            age=16,
            location='sobral',
            fv_color='gray',
            pet='cat',
            pgm_language='python'
            )

user2 = User(
            'emilly',
            'nascimento',
            'do',
            fv_color='yellow',
            age=8,
            location='sobral',
            likes='play and eat candy'
            )

user3 = User('john',
             'doe',
             fv_color='blue',
             works='loremimpsilum dorem',
             location='unknown'
             )

print('-' * 50)
user1.describe_user()
user1.greet_user()
print()
user2.describe_user()
user2.greet_user()
print()
user3.describe_user()
user3.greet_user()
