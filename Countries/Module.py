import random

# Text-to-Speech
from gtts import gTTS
from os import path, remove, system

# Dictionaries
country_capital_dict = {}
capital_country_dict = {}
country = []

# Read data from file
def file_to_dict():
    with open(r'C:\Users\ADMIN\source\repos\HomeWork\Countries\Capital.txt', 'r', encoding='utf-8-sig') as file:
        for line in file:
            k, v = line.strip().split('-')
            country_capital_dict[k] = v
            capital_country_dict[v] = k
            country.append(k)

# Write data to file
def dict_to_file():
    with open(r'C:\Users\ADMIN\source\repos\HomeWork\Countries\Capital.txt', 'w', encoding='utf-8-sig') as file:
        for k, v in country_capital_dict.items():
            file.write(f"{k}-{v}\n")

# Search for a country or capital
def search(Name: str):
    if Name in country_capital_dict:
        answer = country_capital_dict[Name]
    elif Name in capital_country_dict:
        answer = capital_country_dict[Name]
    else:
        answer = "We don't have that Country or Capital in our Dictionary"
    print(answer)

# Add new country-capital pair
def add_to_dict(country: str, capital: str):
    if country in country_capital_dict or capital in capital_country_dict:
        print("This entry already exists!")
        return
    capital_country_dict[capital] = country
    country_capital_dict[country] = capital
    print(f'The dictionary has been updated.')
    dict_to_file()

# Correct a country name
def change_dict_country(Error_Name: str, Right_Name: str):
    if Error_Name not in country_capital_dict:
        print("Country not found!")
        return
    Capital = country_capital_dict.pop(Error_Name)
    del capital_country_dict[Capital]
    country_capital_dict[Right_Name] = Capital
    capital_country_dict[Capital] = Right_Name
    dict_to_file()

# Correct a capital name
def change_dict_capital(Error_Name: str, Right_Name: str):
    if Error_Name not in capital_country_dict:
        print("Capital not found!")
        return
    Country = capital_country_dict.pop(Error_Name)
    del country_capital_dict[Country]
    country_capital_dict[Country] = Right_Name
    capital_country_dict[Right_Name] = Country
    dict_to_file()

# Quiz function to test user knowledge
def country_capital_test():
    countries = list(country_capital_dict.keys())
    capitals = list(capital_country_dict.keys())

    if len(countries) < 5:
        print("Not enough data to run a quiz.")
        return

    # Shuffle the countries
    random.shuffle(countries)
    score = 0

    print("\n--- Country to Capital Quiz ---")
    for i in range(5):
        country = countries[i]
        answer = input(f"What is the capital of {country}? ").strip()
        correct_answer = country_capital_dict[country]
        if answer.lower() == correct_answer.lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {correct_answer}.")

    print("\n--- Capital to Country Quiz ---")
    random.shuffle(capitals)
    for i in range(5):
        capital = capitals[i]
        answer = input(f"{capital} is the capital of which country? ").strip()
        correct_answer = capital_country_dict[capital]
        if answer.lower() == correct_answer.lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {correct_answer}.")

    print(f"\nFinal Score: {score}/10 ({score * 10}%)")

# Load dictionary data on start
file_to_dict()
