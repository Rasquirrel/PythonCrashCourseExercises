def make_car(manufacturer, model, **additional):
    car = {'manufacturer': manufacturer, 'model': model}

    for key, value in additional.items():
        car[key] = value

    return car


my_car = make_car('ashua', 'hasudhasd', color='purple', motor='cavalo')

print(my_car)
