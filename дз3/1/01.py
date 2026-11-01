while True:
   task =input("Давай считать: ")

   if "+" in task:
     a, b = task.split("+")
     a = float(a)
     b = float(b)
     print("Ответ: ", f"{a + b:g}")

   elif "-" in task:
     a, b = task.split("-")
     a = float(a)
     b = float(b)
     print("Ответ: ", f"{a - b:g}")

   elif "*" in task:
     a, b = task.split("*")
     a = float(a)
     b = float(b)
     print("Ответ: ", f"{a * b:g}")

   elif "/" in task:
     a, b = task.split("/")
     a = float(a)
     b = float(b)

     if b != 0:
      print("Ответ: ", f"{a / b:g}")
     else:
      print("на ноль делить нельзя")

   answer = input("Дальше? y/n: ")

   if answer != "y":
    exit()