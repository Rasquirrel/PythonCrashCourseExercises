sandwich_orders = ['ashua sandwich', 'aplle sandwich', 'bacon sandwich', 'healthy sandwich']
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()

    print("\nI made your " + sandwich.title() + ".")

    finished_sandwiches.append(sandwich)

print("\nThese are the finished sandwiches:  ")
for sandwich in finished_sandwiches:
    print(sandwich.title())
