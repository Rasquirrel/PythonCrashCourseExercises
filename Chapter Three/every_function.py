colors = []

print('This is my favorite colors list: ')
print(colors)
print("It's empty now but I will fill it.")

colors.append('blue') 
print('I put one color:')

print(colors)

colors.append('green')

print('I put another color:')
print(colors)

colors.insert(2, 'red')
print('I put red now: ')
print(colors)

del colors[2]
print('I deleted red: ')
print(colors)

color_removed = colors.pop(1)
print('Now I removed ' + color_removed + ':')
print(colors)

colors.remove('blue')
print('Now, I removed blue:')
print(colors)

colors.append('purple')
colors.append('yellow')
colors.append('gray')
colors.append('pink')
colors.append('black')
colors.append('magent')
colors.append('dark-blue')

print('Now I added some of my favorite colors, look: ')
print(colors)

print('Now I will sort this list alphabeticaly, but without change the order permanently')
print(sorted(colors))
print('Look, my list still the sames')
print(colors)

print('Now I will sort this list alphabeticaly reversed but without change the order permanently')
print(sorted(colors, reverse = True))
print('Look, my list still the sames: ')
print(colors)

print('Now I will reverse the order of this list:')
colors.reverse()
print(colors)
colors.reverse()
print('And I will reverse it again to come back to normal:')
print(colors)

print('Now I will sort this list alphabeticaly and permanently')
colors.sort()
print('Look')
print(colors)
print('Now I will sort this list alphabeticaly and permanently and reverse')
colors.sort(reverse = True)
print(colors)

print('This is the end of the program. Congratulations, Isac. You are great! : )')
