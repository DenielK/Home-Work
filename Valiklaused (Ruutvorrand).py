import math

#1 
try:
    number = float(input('Enter the number'))
    if number > 0:
        if number % 2 == 0:
            print('even')
        elif number % 2 == 1:
            print('odd')
        else:
            print('error ex 1 %')
except:
    print('error ex1')

#2
try:
    num1, num2, num3 = float(input('Please enter number 1')), float(input('Please enter number 2')), float(input('Please enter number 3'))
    if num1 > 0 and num2 > 0 and num3 > 0:
        if num1 + num2 + num3 == 180:
            largestnum = max(num1, num2, num3)
            if largestnum < 90:
                print('Остроугольные')
            elif num1 == 90 or num2 == 90 or num3 == 90:
                print('Прямоугольные')
            else:
                print('Тупоугольные')
        else:
            print('not a triangle')
    else:
         print('not a triangle')
except:
    print('error ex 2')
#3
yesORno = input('do you want to know name of the week day by number "yes or no"')
if yesORno.upper() == 'YES':
    numDayOfWeek = int(input('Enter the number day of week (1 - 7)'))
    if numDayOfWeek == 1:
        print('Monday')
    elif numDayOfWeek == 2:
        print('Tuesday')
    elif numDayOfWeek == 3:
        print('Wednesday')
    elif numDayOfWeek == 4:
        print('Thursday')
    elif numDayOfWeek == 5:
        print('Friday')
    elif numDayOfWeek == 6:
        print('Saturday')
    elif numDayOfWeek == 7:
        print('Sunday')
    else:
        print('error ex 3')
elif yesORno.upper() == 'NO':
    print('good bye')
else:
    print('error')
#4
try:
    DateOfBirth = input('Enter you birthay date "yyyy-mm-dd"')
    monthex4, dayex4  = int(DateOfBirth[5:7]), int(DateOfBirth[8:10])
    if monthex4 > 12 or dayex4 > 31:
        print('error ex4')
    elif (monthex4 == 3 and dayex4 >= 21) or (monthex4 == 4 and dayex4<= 19):
        print('Овен (Aries)')
    elif (monthex4 == 4 and dayex4 >= 20) or (monthex4 == 5 and dayex4 <= 20):
        print('Телец (Taurus)')
    elif (monthex4 == 5 and dayex4 >= 21) or (monthex4 == 6 and dayex4 <= 21):
        print('Близнецы (Gemini)')
    elif (monthex4 == 6 and dayex4 >= 22) or (monthex4 == 7 and dayex4 <= 22):
        print('Рак (Cancer)')
    elif (monthex4 == 7 and dayex4 >= 23) or (monthex4 == 8 and dayex4 <= 22):
        print('Лев (Leo)')
    elif (monthex4 == 8 and dayex4 >= 23) or (monthex4 == 9 and dayex4 <= 22):
        print('Дева (Virgo)')
    elif (monthex4 == 9 and dayex4 >= 23) or (monthex4 == 10 and dayex4 <= 23):
        print('Весы (Libra)')
    elif (monthex4 == 10 and dayex4 >= 24) or (monthex4 == 11 and dayex4 <= 21):
        print('Скорпион (Scorpio)')
    elif (monthex4 == 11 and dayex4 >= 22) or (monthex4 == 12 and dayex4 <= 21):
        print('Стрелец (Sagittarius)')
    elif (monthex4 == 12 and dayex4 >= 22) or (monthex4 == 1 and dayex4 <= 20):
        print('Козерог (Capricorn)')
    elif (monthex4 == 1 and dayex4 >= 21) or (monthex4 == 2 and dayex4 <= 20):
        print('Водолей (Aquarius)')
    elif (monthex4 == 2 and dayex4 >= 21) or (monthex4 == 3 and dayex4 <= 20):
        print('Рыбы (Pisces)')
    else:
        print('error ex 4 h')
except:
    print('error ex 4 try')
#5
try:
    enterdataex5 = input('enter number or text')
    if enterdataex5.isalpha() == True:
        print('Text')
    elif enterdataex5.isidentifier() == True:
        enterdataex5 = float(enterdataex5)
        print(enterdataex5 * 0.7)
    elif enterdataex5.isnumeric() == True:
        enterdataex5 = float(enterdataex5)
        print(enterdataex5 * 0.5)
except:
    print('error ex5')

#6
yesORno = input('do you want to solve a quadratic level "yes or no"')
if yesORno.upper() == 'YES':
    aEx6, bEx6, cEx6 = float(input('Enter a')), float(input('Enter b')), float(input('Enter c'))
    Dex6 = (bEx6 ** 2) - 4 * aEx6 * cEx6
    if Dex6 > 0:
        print(Dex6)
        x1Ex6 =(- bEx6 + math.sqrt(Dex6)) / (2 * aEx6)
        x2Ex6 =(- bEx6 - math.sqrt(Dex6)) / (2 * aEx6)
        print(x1Ex6, x2Ex6)
    elif Dex6 == 0:
        xEx6 = -bEx6 / (2 * aEx6)
        print(xEx6)
    elif Dex6 < 0:
        print('net kornei')
    else:
        print('error ex6 D')