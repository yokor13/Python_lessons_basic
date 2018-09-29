
__author__ = 'Коростылев Владислав Олегович'

# Задача-1: Дано произвольное целое число, вывести самую большую цифру этого числа.
# Например, дается x = 58375.
# Нужно вывести максимальную цифру в данном числе, т.е. 8.
# Подразумевается, что мы не знаем это число заранее.
# Число приходит в виде целого беззнакового.
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании и понимании решите задачу с применением цикла for.

n = 0
x = input ("Запишите число: ")
for a in x:
    if int (a) > int (n):
        n = a
print (n)

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
# Подсказки:
# * постарайтесь сделать решение через действия над числами;
# * при желании и понимании воспользуйтесь синтаксисом кортежей Python.
z = (input ("Запишите число1: "), input ("Запишите число2: "))

print (z[1] + " " + z[0])

# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax² + bx + c = 0.
# Коэффициенты уравнения вводятся пользователем.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math:
# import math
# math.sqrt(4) - вычисляет корень числа 4

a = int (input ("ax² + bx + c = 0 " + "Запишите число a: "))
b = int (input ("Запишите число b: "))
c = int (input ("Запишите число c: "))
d = b**2-4*a*c

if a==0:
    y=-c/b
    print ("Это же не квадратное уравнение!!! В таком случае ответ:",y)

import math
if d > 0:
    y = (-b-math.sqrt(d))/(2*a)
    x = (-b+math.sqrt(d))/(2*a)
    print ("Два корня: ", y, x)

if d==0:
    y =-b/(2*a)
    print ("Один корень: ", y)

if d<0:
    print ("Корней нет")

