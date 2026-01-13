cart = []
cart.append(("Чайник", 500))
cart.append(("Кава", 150))

for item in cart:
    print(item[0], item[1])

total = sum(item[1] for item in cart)
print("Всього:", total)
