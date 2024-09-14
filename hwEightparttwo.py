
num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))


sum_lambda = lambda x, y: x + y

result = sum_lambda(num1, num2)
print("Сумма двух чисел:", result)
