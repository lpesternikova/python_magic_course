# 4) Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

 # Пример:

# 6782 -> 23
# 0,56 -> 11

num = float(input())
result = 0

while num != 0:
    if num > 0 and num % 1 > 1 :
        result = result + (num % 10)
        num = num // 10
    else: 
        print("Дробное!") 
        
print(result)

