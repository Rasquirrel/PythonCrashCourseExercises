favorite_foods = ['pizza', 'falafel', 'carrot cake', 'cannoli']
friend_favorites = favorite_foods[:3]

friend_favorites.append('ice cream')

print('My favorite foods are: ')
for food in favorite_foods:
    print(food.title())

print("My friend's favorite foods are: ")
for food in friend_favorites:
    print(food.title())
        