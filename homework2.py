# Задача 10: На столе лежат n монеток. 
#  Некоторые из них лежат вверх решкой, а некоторые – гербом. 
#  Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
#  Выведите минимальное количество монет, которые нужно перевернуть

# from random import randint
# count = int(input("Введите количество монет: "))
# i = 0
# countHeads = 0
# countTails = 0
# for i in range(count):
#     if randint(0,2): countHeads += 1
#     else: countTails += 1    
# print(f"Требуется перевернуть {min(countHeads,countTails)} монет")


# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. 
#  Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. 
#  Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. 
#  Помогите Кате отгадать задуманные Петей числа.

# sum = int(input("Сумма: "))
# mult = int(input("Произведение: "))
# if sum**2 - 4*mult >= 0: 
#     d = (sum**2 - 4*mult)**(1/2)
#     x1 = (sum - d)/2
#     if x1 == int(x1):
#         x2 = (sum + d)/2
#         print(f"Загаданы числа {int(x1)} и {int(x2)}")
#     else: print("Пары целых чисел не существует")
# else: print("Пары действительных чисел не существует")    


# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2**k), не превосходящие числа N.

# number = int(input("Введите число: "))
# exp2 = 1
# while exp2 <= number:
#     print(exp2, end=" ")
#     exp2 *= 2