#Напишите программу, которая принимает на вход цифру, обозначающую день недели, 
#и проверяет, является ли этот день выходным.
a = int(input('Введите день недели (с 1 по 7): '))
if (a == 6 or a == 7):
    print('yes')
else:
    print('no')