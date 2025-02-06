from random import *
#test
count = 0
levelofmath = int(input('Please enter level complexity of the math "1 - easy, 2 - medium, 3 - hard": '))

if levelofmath == 1:
    quantityofex = int(input('Please enter the quantity of exercises: '))
    print('You chose level easy (Only integer numbers)')
    for _ in range(quantityofex):
        mathOperator = randint(1, 2)
        num1, num2 = randint(1, 10), randint(1, 10)

        if mathOperator == 1:
            print(f'Number 1: {num1}, Number 2: {num2}, Math operator "+"')
            answer = int(input('Please enter the answer: '))
            rightanswer = num1 + num2
        else:
            print(f'Number 1: {num1}, Number 2: {num2}, Math operator "-"')
            answer = int(input('Please enter the answer: '))
            rightanswer = num1 - num2

        if rightanswer == answer:
            print('You are right')
            count += 1
        else:
            print(f'Wrong, right answer was {rightanswer}')

elif levelofmath == 2:
    quantityofex = int(input('Please enter the quantity of exercises: '))
    for _ in range(quantityofex):
        mathOperator = randint(1, 4)
        num1, num2 = randint(10, 20), randint(10, 20)

        if mathOperator == 1:
            print(f'Number 1: {num1}, Number 2: {num2}, Math operator "+"')
            answer = int(input('Please enter the answer: '))
            rightanswer = num1 + num2
        elif mathOperator == 2:
            print(f'Number 1: {num1}, Number 2: {num2}, Math operator "-"')
            answer = int(input('Please enter the answer: '))
            rightanswer = num1 - num2
        elif mathOperator == 3:
            print(f'Number 1: {num1}, Number 2: {num2}, Math operator "*"')
            answer = float(input('Please enter the answer: '))
            rightanswer = num1 * num2
        else:
            print(f'Number 1: {num1}, Number 2: {num2}, Math operator "/"')
            answer = float(input('Please enter the answer with two decimal places: '))
            rightanswer = round(num1 / num2, 2)

        if rightanswer == answer:
            print('You are right')
            count += 1
        else:
            print(f'Wrong, right answer was {rightanswer}')

elif levelofmath == 3:
    quantityofex = int(input('Please enter the quantity of exercises: '))
    for _ in range(quantityofex):
        num1, num2, num3 = randint(10, 100), randint(1, 100), randint(1, 50)
        mathOperator = randint(1, 4)

        if mathOperator == 1:
            print(f'{num1} : {num2} + {num3}')
            answer = float(input('Enter answer with two decimal places: '))
            rightanswer = round(num1 / num2 + num3, 2)
        elif mathOperator == 2:
            print(f'{num1} * {num2} - {num3}')
            answer = float(input('Enter answer with two decimal places: '))
            rightanswer = round(num1 * num2 - num3, 2)
        elif mathOperator == 3:
            print(f'{num1} + {num2} * {num3}')
            answer = float(input('Enter answer with two decimal places: '))
            rightanswer = round(num1 + num2 * num3)
        else:
            print(f'{num1} - {num2} * {num3}')
            answer = float(input('Enter answer with two decimal places: '))
            rightanswer = round(num1 - num2 * num3)

        if rightanswer == answer:
            print('You are right')
            count += 1
        else:
            print(f'Wrong, right answer was {rightanswer}')

print(count)
grade = (count / quantityofex) * 100
print(f'{grade} %')

if grade < 60:
    print('Your grade 2')
elif grade < 75:
    print('Your grade 3')
elif grade < 90:
    print('Your grade 4')
else:
    print('Your grade 5')
