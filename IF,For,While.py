try:
    a, b, h = None, None, None
    a, b, h = float(input('Enter A - ')), float(input('Enter B - ')), float(input('Enter H - '))
except:
    print('error')
if a is not None and b is not None and h is not None:
    S = (a + b) * h / 2
    print(S)
else:
    print('valiable is empty')

# 1
quantitiesOfNumbers = None
try:
    quantitiesOfNumbers = int(input('Enter quantity of numbers: '))
    if quantitiesOfNumbers is not None:
        maxnum = 0
        for x in range(quantitiesOfNumbers):
            x = float(input('Enter number: '))
            if x > maxnum:
                maxnum = x
        print(f'{maxnum} The biggest number: ')
    else:
        print('Variable is empty')

except:
    print('error only int')
# 2
intnumber = None
try:
    intnumber = int(input('Enter INT number: '))
    if intnumber is not None:
        if intnumber == 13:
            intnumber = 77
        print(intnumber)
except:
    print('error ex 2')
# 3 
startday = 10
daylypercent = 0.10
days = 7
for x in range(days):
    startday = startday + startday * daylypercent
    print(f'Day number {x} distance {round(startday, 2)}')
# 4
lengthOfCloth = None
try:
    lengthOfCloth = float(input('Enter Length of Cloth '))
    if lengthOfCloth is not None:
        while 1:
            lengthOfSlice = float(input('Enter Length of Cloth '))
            if lengthOfSlice > lengthOfCloth:
                print(f'Lack of material')
                YesOrNo = input(f'Would you like to buy {lengthOfCloth} "Yes or No" - ')
                if YesOrNo.upper() == 'YES':
                    print('Thank you for purchase')
                    exit()
                elif YesOrNo.upper() == 'NO':
                    print('Next client')
                else:
                    print('You can enter only Yes or No - ')
            elif lengthOfCloth == 0:
                print('The material run out')
            else:
                lengthOfCloth = lengthOfCloth - lengthOfSlice
    else:
        print('Variable empty')
except:
    print('error')
# 5
while True:
    YesOrNo = input('Do you want finish program "yes" or "no" - ')
    if YesOrNo.lower() == 'yes':
        break
    elif YesOrNo.lower() == 'no':
        try:
            a, b, h = None, None, None
            a, b, h = float(input('Enter A - ')), float(input('Enter B - ')), float(input('Enter H - '))
        except:
            print('error')
        if a is not None and b is not None and h is not None:
            S = (a + b) * h / 2
            print(S)
        else:
            print('valiable is empty')
    else:
        print('Error')
# 6
numberEx6 = float(input('Enter the number (number % 3 == 0) - '))
numberEx6Residue = numberEx6 % 3
if numberEx6Residue == 0:
    print(f'{numberEx6} % 3 = {numberEx6Residue}')
else:
    print("divide with remainder")

    #corrections
