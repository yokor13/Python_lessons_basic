
__author__ = "Коростылев Владислав Олегович"

# Задача-1: Дано произвольное целое число (число заранее неизвестно).
# Вывести поочередно цифры исходного числа (порядок вывода цифр неважен).
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании решите задачу с применением цикла for.

# код пишем тут...
x = input ("Запишите число: ")
for a in x: # Перебор цифр
    print(a) # Вывод цифр

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Подсказка:
# * постарайтесь сделать решение через дополнительную переменную 
#   или через арифметические действия
# Не нужно решать задачу так:
# print("a = ", b, "b = ", a) - это неправильное решение!
z = input ("Запишите число1: ")
y = input ("Запишите число2: ")
w = y + " " + z

print (w)


# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"

u = int (input ("Ваш возраст?: "))
if u > 18:
    print ("Доступ разрешен")
else:
    print ("Извините, пользование данным ресурсом только с 18 лет")