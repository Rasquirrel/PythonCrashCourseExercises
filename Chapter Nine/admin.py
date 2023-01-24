from user import User

class Privileges:
    """Privileges of the admin"""
    def __init__(self, privileges=['can add post', 'can remove post', 'can ban a user']):
        self.privileges = privileges
    
    def show_privileges(self):
        """Show admin's privileges"""
        print("These are the admin's privileges: ")
        for privilege in self.privileges:
            print('\t ' + privilege.capitalize())
 

class Admin(User):
    """Attempt to build a admin"""

    def __init__(self, first_name, last_name, middle_name='', **user_info):
        """Initialize atributes."""
        super().__init__(first_name, last_name, middle_name, **user_info)
        self.privileges = Privileges()
        self.is_admin = True
    
   
    def describe_user(self):
        """Prints all information about the admin"""
        print('These are the info about user: ' + self.full_name.title())
        print('\tIs Admin: ' + str(self.is_admin).title())
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
        print('Hello ' + self.first_name.title() + '! Is a pleasure to ',
                                              'see you again, admin.')
