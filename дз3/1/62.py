number = int(input("Введите число: "))

days = number // 86400
hours = number % 86400 // 3600
minutes = number % 3600 // 60
seconds = number % 60

print(f"{days} дн., {hours:02} ч., {minutes:02} мин., {seconds:02} сек.")