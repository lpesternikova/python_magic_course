# 5) Напишите код, который запрашивает число и сообщает является ли оно простым или составным. 
# Используйте правило для проверки: “Число является простым, 
# если делится нацело только на единицу и на себя”. 
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

num = int(input())

if num >= 0 and num <= 100000:
    prime_num = True
    for i in range (2, num // 2 + 1):
        if num % i == 0:
            print("Это составное число!")
            prime_num = False
            break
    if prime_num:
            print("Это простое число!")
else:
    print("Это число не подходит!")
