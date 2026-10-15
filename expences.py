food = input("введите траты на еду: ")
car = input("введите траты на транспорт: ")
fun = input("введите траты на развлечения: ")

summ = sum((int(food), int(car), int(fun)))

print(summ)
print(summ / 3)
#изменение1