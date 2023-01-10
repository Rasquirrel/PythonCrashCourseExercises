sandwich_orders = ['pastrami', 'pastrami', 'bacon', 'cheese', 'salmon', 'candy']

print("The Deli has runned out of pastrami.\n")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print("\nThese are the sandwich orders: \n")
for sandwich in sandwich_orders:
    print(sandwich.title() + " sandwich.")
