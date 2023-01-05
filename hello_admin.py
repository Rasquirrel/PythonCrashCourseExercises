users = ['isac', 'emilly', 'igor', 'sales', 'admin']

for user in users:
    if user == 'admin':
        print('Olá ' + user.title() + ', você gostaria de visualizar o painel de status?')
    else:
        print('Olá ' + user.title() + ', seja bem-vindo. Obrigado por se conectar novamente.')
