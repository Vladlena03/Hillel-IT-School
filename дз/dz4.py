price = float(input("Введите цену: "))
discount = float(input("Введите скидку (%): "))
final_price = price - (price*discount/100)
print("Цена со скидкой:", final_price)