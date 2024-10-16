# 4) Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

 # Пример:

# 6782 -> 23
# 0,56 -> 11

num = abs(float(input()))

while num % 1 != 0:
    num = num * 10

num = int(num)

result = 0
while num > 0:
    result = result + num % 10
    num = num // 10

print(result)

