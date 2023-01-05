current_users = ['isac', 'ludimila', 'neide', 'raimundo', 'simao']

new_users = ['Isac', 'ludimila', 'emilly', 'sales', 'simao']

for new_user in new_users:
   if new_user.lower().strip() in current_users:
        print('Sorry, user name ' + new_user + ' already taken.')
   else:
        print(new_user  +' is avaliable, welcome!')
