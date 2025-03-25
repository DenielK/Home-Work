from Module import *
if __name__ == "__main__": 
    file_to_dict()
while True:
    # text_to_speech('1 - Search, 2 - Add Country and Capital to Dictionary', 'English')
    print('1 - Search, 2 - Add Country and Capital to Dictionary')
    print('3 - Change Dictionary 4 - Test')
    answer = None
    try:
        answer = int(input('Enter the number - '))
    except:
        print('Error only INT numbers')
    if answer == 1:
        Name = input('Enter Contry or Capital - ')
        search(Name)
    elif answer == 2:
        Country = input('Enter Country - ')
        Capital = input('Enter Capital - ')
        add_to_dict(Country, Capital)
    elif answer == 3:
        AorB = input('Do you want change Country - A or Capital - B ').upper()
        Error_Name = input('Enter wrong name ')
        Right_Name = input('Enter Right name ')
        if AorB == 'A':
            change_dict_country(Error_Name, Right_Name)
        elif AorB == 'B':
            change_dict_capital(Error_Name, Right_Name)
        else:
            print('Error')
    elif answer == 4:
        country_capital_test()