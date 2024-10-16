# 5) Напишите код, который запрашивает число и сообщает является ли оно простым или составным. 
# Используйте правило для проверки: “Число является простым, 
# если делится нацело только на единицу и на себя”. 
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

num = int(input())
new_num = int(input())

if num >= 0 and num <= 100000:
    while new_num < num:
        new_num = new_num + 1
        if num % 1 == 0 and num % num == 0 and num % new_num != 0:
            print("Это простое число!")
        else:
            print("Это составное число!")
else:
    print("Это число не подходит!")
