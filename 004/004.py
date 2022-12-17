#Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
def Distance2D(xa, ya, xb, yb):
    if xa > xb:
        x_len = xa-xb
    else: x_len = xb-xa

    if ya > yb:
        y_len = ya-yb
    else: y_len = yb-ya

    Distance = (x_len**2 + y_len**2)**0.5

    return Distance


res = Distance2D(10, 50, 30, 40)
print ('%.2f'%(res))