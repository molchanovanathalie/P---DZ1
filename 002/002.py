#Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

x = int(input('Введите x : '))
y = int(input('Введите y : '))
if(x > 0 and y > 0):
    print('Первая четверть')
if(x < 0 and y > 0):
    print('Вторая четверть')
if(x < 0 and y < 0):
    print('Третья четверть')
if(x > 0 and y < 0):
    print('Четвертая четверть')