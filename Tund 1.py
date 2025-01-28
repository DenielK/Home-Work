
from random import * # * - все фунции или можно написать только функцию если хочешь переименовать фунцию можно использовать
# randint as rd - examlpleэ
from math import *
#1
print('tere tulemast')
nimi =input("Mis on sinu nimi? ").capitalize() #lower(), upper(), /
print('Tere tulemast! Tervitan sind ', nimi)
print('Tere tulemast! Tervitan sind '+ nimi)
try:
    vanus=int(input("kui vana sa oled? "))
    print("Tere tulemast! Tervitan sind "+nimi+" Sa oled ",vanus,'aastat vana')
    print(f"Tere tulemast! Tervitan sind {nimi} Sa oled {vanus} aastat vana")
except:
    print('error')




#2
vanus = 18
eesnimi = "Jaak"
pikkus = 16.5
kas_käib_koolis = True
print(type(vanus)), print(type(eesnimi)), print(type(pikkus)), print(type(kas_käib_koolis))

#3
kokku=randint(1,1000)
print(kokku)
kommi=int(input('mittu kommi '))
kokku=kokku-kommi
print(f'jaak on {kokku} kommi ')

#4
l = int(input('Enter umbermoot - '))
d=l/pi
print(round(d, 2))

#5
N = float(input("Введите N "))
M = float(input("Введите M "))
S = N*M
print(S, ' Длинна прямоугольного участка')

#6 

aeg = float(input("Mitu tundi kulus sõiduks? "))
teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
kiirus = teepikkus / aeg 
print("Sinu kiirus oli " + str(kiirus) + " km/h")

#7

N1, N2, N3, N4, N5 = float(input('Введите число 1 - ')), float(input('Введите число 2 - ')), float(input('Введите число 3 - ')), float(input('Введите число 4 - ')), float(input('Введите число 5 - '))
print((N1 + N2 + N3 + N4 + N5) / 5, "среднее")

#8

print('    @..@\n   (----)\n  ( \\__/ )\n  ^^ «» ^^  ')

#9 
print('Вычисляем периметр треугольника введи все данные')
A, B, C = float(input('Enter A - ')), float(input('Enter B - ')), float(input('Enter C - '))
print('P = ',A + B + C)

#10

price = float(12.90)
tips = float(0.10)
costforperson = price * tips + price
print('total cost :', round(costforperson, 3), 'euro, per person ', round(costforperson, 3) / 2, ' euro')