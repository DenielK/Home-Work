import random
from gtts import gTTS
from os import path, remove, system

country_capital_dict = {}  # Словарь, где ключ — страна, а значение — столица
capital_country_dict = {}  # Словарь, где ключ — столица, а значение — страна
country = []  # Список, содержащий все страны

# Функция для чтения данных из файла и добавления их в словари
def file_to_dict():
    with open(r'C:\Users\opilane.TTHK\Desktop\Countries\Capital.txt', 'r', encoding='utf-8-sig') as file:
        for line in file:
            # Убираем пробелы и символы переноса строк, делим строку по символу "-"
            k, v = line.strip().split('-')
            # Добавляем пару "страна-столица" в словарь country_capital_dict
            country_capital_dict[k] = v
            # Добавляем пару "столица-страна" в словарь capital_country_dict
            capital_country_dict[v] = k
            country.append(k)

# Функция для записи данных из словаря в файл
def dict_to_file():
    with open(r'C:\Users\opilane.TTHK\Desktop\Countries\Capital.txt', 'w', encoding='utf-8-sig') as file:
        for k, v in country_capital_dict.items():
            file.write(f"{k}-{v}\n")# Записываем в файл строку в формате "страна-столица"

# Функция для поиска страны или столицы
def search(Name: str):
    # Проверяем, есть ли в словаре страна с таким названием
    if Name in country_capital_dict:
        answer = country_capital_dict[Name]  # Получаем столицу по стране
    # Проверяем, есть ли в словаре столица с таким названием
    elif Name in capital_country_dict:
        answer = capital_country_dict[Name]  # Получаем страну по столице
    else:
        answer = "We don't have that Country or Capital in our Dictionary" 
    print(answer)

# Функция для добавления новой пары страна-столица
def add_to_dict(country: str, capital: str):
    if country in country_capital_dict or capital in capital_country_dict: #провека на существование пары в словарях
        print("This entry already exists!")
        return
    # Добавляем новую пару в оба словаря
    capital_country_dict[capital] = country
    country_capital_dict[country] = capital
    print(f'The dictionary has been updated.')
    dict_to_file()

# Функция для исправления названия страны
def change_dict_country(Error_Name: str, Right_Name: str):
    # Проверяем, существует ли указанная страна
    if Error_Name not in country_capital_dict:
        print("Country not found!") 
        return
    # Получаем столицу для ошибки и удаляем старую запись
    Capital = country_capital_dict.pop(Error_Name)
    del capital_country_dict[Capital]
    # Добавляем исправленную страну с тем же названием столицы
    country_capital_dict[Right_Name] = Capital
    capital_country_dict[Capital] = Right_Name
    dict_to_file()

# Функция для исправления названия столицы
def change_dict_capital(Error_Name: str, Right_Name: str):
    # Проверяем, существует ли указанная столица
    if Error_Name not in capital_country_dict:
        print("Capital not found!")
        return
    # Получаем страну для ошибки и удаляем старую запись
    Country = capital_country_dict.pop(Error_Name)
    del country_capital_dict[Country]
    # Добавляем исправленную столицу с тем же названием страны
    country_capital_dict[Country] = Right_Name
    capital_country_dict[Right_Name] = Country
    dict_to_file()  # Записываем изменения в файл

# Функция для теста на знание стран и столиц
def country_capital_test():
    countries = list(country_capital_dict.keys())
    capitals = list(capital_country_dict.keys())

    # Если стран слишком мало для проведения теста, выводим предупреждение
    if len(countries) < 5:
        print("Not enough data to run a quiz.")
        return

    # Перемешиваем список стран случайным образом
    random.shuffle(countries)
    score = 0

    # Тест на знание стран и столиц
    print("\n--- Country to Capital Quiz ---")
    for i in range(3):
        # Берем страну из перемешанного списка
        country = countries[i]
        # Спрашиваем пользователя столицу этой страны
        answer = input(f"What is the capital of {country}? ").strip()
        correct_answer = country_capital_dict[country]  # Правильный ответ
        # Проверяем ответ пользователя
        if answer.lower() == correct_answer.lower():
            print("Correct!")
            score += 1  # Увеличиваем счет за правильный ответ
        else:
            print(f"Wrong! The correct answer is {correct_answer}.")

    # Тест на знание столиц и стран
    print("\n--- Capital to Country Quiz ---")
    random.shuffle(capitals)  # Перемешиваем список столиц
    for i in range(2):
        # Берем столицу из перемешанного списка
        capital = capitals[i]
        # Спрашиваем пользователя, какая страна является этой столицей
        answer = input(f"{capital} is the capital of which country? ").strip()
        correct_answer = capital_country_dict[capital]  # Правильный ответ
        # Проверяем ответ пользователя
        if answer.lower() == correct_answer.lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {correct_answer}.")

    print(f"\nFinal Score: {score}/5 ({score * 20}%)")

file_to_dict()
