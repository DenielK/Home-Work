from datetime import *  

ikoodid = []  # Список для хранения правильных кодов.
arvud = []  # Список для хранения неправильных кодов.
esarv = ['1', '2', '3', '4', '5', '6']  # Список возможных первых цифр для определения пола и года.
today = datetime.now().date()  # Получаем текущую дату.
year = today.year - 2000  # Извлекаем текущий год (последние 2 цифры).
month = today.month  # Извлекаем текущий месяц.
day = today.day  # Извлекаем текущий день.
esastme = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]  
teineastme = [3, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3]
naine = ['2', '4', '6']  # Список, определяющий женский пол по первой цифре.
mees = ['1', '3', '5']  # Список, определяющий мужской пол по первой цифре.

while True:  
    ik = str(input("Sisesta isikukood (süsteemi peatumiseks sisesta X): "))
    print()
    if ik.upper() == "X":  # Если пользователь вводит X, программа завершает работу.
        break
    else:
        if len(ik) == 11 and ik.isdigit():  # Проверяем, что код состоит из 11 цифр.
            if ik[0] in esarv:  # Проверяем, что первая цифра — валидная (1-6).
                if (ik[0] in ['1', '2', '3', '4']) or (ik[0] in ['5', '6'] and int(ik[1:3]) <= year):  # Проверка на год (особенно для будущих лет).
                    if 0 < int(ik[3:5]) <= 12:  # Проверка на месяц.
                        if 0 < int(ik[5:7]) <= 31:  # Проверка на день.
                            esastmesumm = 0 
                            for i in range(10):  # Проходим по всем цифрам, кроме контрольной.
                                summ = int(ik[i]) * esastme[i]  # Умножаем цифры на соответствующие множители.
                                esastmesumm += summ  # Суммируем.
                            esjaak = esastmesumm % 11  # Находим остаток от деления на 11.
                            kontroll = None  # Инициализация переменной контролля
                            if esjaak != 10:  # Если остаток не 10, то это контрольная цифра.
                                kontroll = esjaak
                            elif esjaak == 10:  # Если остаток 10, то используем вторую схему.
                                teineastmesumm = 0
                                for i in range(10):
                                    summ = int(ik[i]) * teineastme[i]  # Расчёт по второй схеме.
                                    teineastmesumm += summ
                                teinejaak = teineastmesumm % 11  # Находим остаток от деления на 11.
                                teinekontroll = None  # Инициализация второй контрольной цифры.
                                if teinejaak != 10:
                                    teinekontroll = teinejaak
                                elif teinejaak == 10:
                                    teinekontroll = 0  # Если остаток 10, то контрольная цифра = 0.

                            if kontroll is not None and kontroll == int(ik[10]):  # Сравниваем полученную контрольную цифру с последней цифрой кода.
                                print(f"Isikukood: {ik}\nKontrollnumber on õige:\nKontrollnumber on: {kontroll}\nIsikukoodi viimane number on: {ik[10]}")
                                print()
                                # Определение места рождения по цифрам кода.
                                if 0 < int(ik[7:10]) <= 10:
                                    haigla = "Kuressaare Haigla"
                                    print("Isikukood on õige")
                                    ikoodid.append(ik)
                                elif 11 <= int(ik[7:10]) <= 19:
                                    haigla = "Tartu Ülikooli Naistekliinik, Tartumaa, Tartu"
                                    print("Isikukood on õige")
                                    ikoodid.append(ik)
                                elif 21 <= int(ik[7:10]) <= 220:
                                    haigla = "Ida-Tallinna Keskhaigla, Pelgulinna sünnitusmaja, Hiiumaa, Keila, Rapla haigla, Loksa haigla"
                                    print("Isikukood on õige")
                                    ikoodid.append(ik)
                                elif 221 <= int(ik[7:10]) <= 270:
                                    haigla = "Ida-Viru Keskhaigla (Kohtla-Järve, endine Jõhvi)"
                                    print("Isikukood on õige")
                                    ikoodid.append(ik)
                                # Другие проверки для различных больниц по аналогии.
                                else:
                                    print("Kahjuks isikukood on vale!")
                                    arvud.append(ik)
                                # Определение года рождения.
                                if ik[0] in ['1', '2']:
                                    sunyear = 1800 + int(ik[1:3])
                                elif ik[0] in ['3', '4']:
                                    sunyear = 1900 + int(ik[1:3])
                                else:
                                    sunyear = 2000 + int(ik[1:3])
                                # Определяем пол по первой цифре.
                                if ik[0] in naine:
                                    print(f"See on naine. Ta on sündinud {ik[5:7]}.{ik[3:5]}.{sunyear} ja sünnikoht on {haigla}")
                                    ikoodid.append(ik)
                                if ik[0] in mees:
                                    print(f"See on mees. Ta on sündinud {ik[5:7]}.{ik[3:5]}.{sunyear} ja sünnikoht on {haigla}")
                                    ikoodid.append(ik)
                            else:
                                print("Kahjuks isikukood on vale!")
                                arvud.append(ik)
                        else:
                            print("Sellist kuupäeva ei ole")  # Неверный день.
                            arvud.append(ik)
                    else:
                        print("Sellist kuud ei ole")  # Неверный месяц.
                        arvud.append(ik)
                else:
                    print("selline isikukood võib olla ainult tulevikus")  # Неверный год.
                    arvud.append(ik)
            else:
                print("Esimene sümbol ei ole õige")  # Неверный первый символ.
                arvud.append(ik)
                print()
        else:
            print("Isikukoodis peab olema 11 märgi")  # Код должен содержать 11 цифр.
            arvud.append(ik)
            print()
        
        # Выводим список правильных и неправильных кодов.
        print(f"Õigete isikukoodide loetelu:\n{ikoodid}")  
        print()
        print()
        print(f"Valete isikukoodide loetel:\n{arvud}")
        print()
        print()
