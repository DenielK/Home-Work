from math import * #неправильный порядок слов

print("Ruudu karakteristikud")
a=float(input('Sisesta ruudu külje pikkus => ')) #не было float
S=a**2
print("Ruudu pindala", S)
P=4*a
print("Ruudu ümbermõõt", P) #неправильные скобки были
di=a*sqrt(2) #math было лишним
print(di)
print("Ruudu diagonaal", round(di,2))
print()
print("Ristküliku karakteristikud") #лишняя скобка
b=float(input("Sisesta ristküliku 1. külje pikkus => ")) #тут не хватало float
c=float(input("Sisesta ristküliku 2. külje pikkus => "))
S=b*c
print('Ristküliku pindala', S) # ' не хватало
P=2*(b+c) # знака умножения не было
print("Ristküliku ümbermõõt", P)
di=sqrt(b**2+c**2) # убрал math и добавил * для возведения в степень
print("Ristküliku diagonaal", round(di, 2)) # надо было закрыть скобки и к di поставить округление 2
print()
print("Ringi karakteristikud")
r=float(input("Sisesta ringi raadiusi pikkus => ")) #много лишних ' и надо было добавить float
d=2*r # * не было
print("Ringi läbimõõt", d) # не было ,
S=pi*r**2 # после pi () лишние, * не хватало для возведения в степерь
print("Ringi pindala", round(S, 2)) # 2 в округление добавил
C=2*pi*r # * не было, после pi () лишние
print("Ringjoone pikkus", round(C, 2)) # ) не было, 2 в округление добавил
