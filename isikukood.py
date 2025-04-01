from datetime import *
ikoodid=[]
arvud=[]
esarv=['1','2','3','4','5','6']
today=datetime.now().date()
year=today.year-2000
month=today.month
day=today.day
esastme=[1,2,3,4,5,6,7,8,9,1]
teineastme=[3,2,3,4,5,6,7,8,9,1,2,3]
naine=['2','4','6']
mees=['1','3','5']
while True:
    ik=str(input("Sisesta isikukood (süsteemi peatumiseks sisesta X): "))
    print()
    if ik.upper()=="X":
        break
    else:
        if len(ik)==11 and ik.isdigit():
            if ik[0] in esarv:
                if ik[0] in ['1','2','3','4'] or (ik[0] in ['5','6'] and int(ik[1:3])<=year):
                    if 0<int(ik[3:5])<=12 or (ik[0] in ['5','6'] and int(ik[3:5])<=month):
                        if 0<int(ik[5:7])<=31 or (ik[0] in ['5','6'] and int(ik[5:7])<=day):
                            esastmesumm=0
                            for i in range(10):
                                summ=int(ik[i])*esastme[i]
                                esastmesumm+=summ
                            esjaak=esastmesumm%11
                            if esjaak !=10:
                                kontroll=esjaak
                            elif kontroll==10:
                                teineastmesumm=0
                                for i in range(10):
                                    summ=int(ik[i])*teineastme[i]
                                    teineastmesumm+=summ
                                teinejaak=teineastmesumm%11
                                if teinejaak !=10:
                                    teinekontroll=teinejaak
                                elif teinejaak==10:
                                    teinekontroll=0
                            if kontroll==int(ik[10]):
                                print(f"Isikukood: {ik}\nKontrollnumber on õige:\nKontrollnumber on: {kontroll}\nIsikukkodi viimane number on: {ik[10]}")
                                print()
                                if 0<int(ik[7:10])<=10:
                                    haigla="Kuressaare Haigla"
                                    print("Isikukood on õige")
                                    print()
                                    ikoodid.append(ik)
                                elif 11<=int(ik[7:10])<=19:
                                    haigla="Tartu Ülikooli Naistekliinik, Tartumaa, Tartu"
                                    print("Isikukood on õige")
                                    print()
                                    ikoodid.append(ik)
                                elif 21<=int(ik[7:10])<=220:
                                    haigla="Ida-Tallinna Keskhaigla, Pelgulinna sünnitusmaja, Hiiumaa, Keila, Rapla haigla, Loksa haigla"
                                    print("Isikukood on õige")
                                    print()
                                    ikoodid.append(ik)
                                elif 221<=int(ik[7:10])<=270:
                                    haigla="Ida-Viru Keskhaigla (Kohtla-Järve, endine Jõhvi)"
                                    print("Isikukood on õige")
                                    print()
                                    ikoodid.append(ik)
                                elif 271<=int(ik[7:10])<=370:
                                    haigla="Maarjamõisa Kliinikum (Tartu), Jõgeva Haigla"
                                    print("Isikukood on õige")
                                    print()
                                    ikoodid.append(ik)
                                elif 371<=int(ik[7:10])<=420:
                                    haigla="Narva Haigla"
                                    print("Isikukood on õige")
                                    print()
                                    ikoodid.append(ik)
                                elif 421<=int(ik[7:10])<=470:
                                    haigla="Pärnu Haigla"
                                    print("Isikukood on õige")
                                    print()
                                    ikoodid.append(ik)
                                elif 471<=int(ik[7:10])<=490:
                                    haigla="Pelgulinna Sünnitusmaja (Tallinn), Haapsalu haigla"
                                    print("Isikukood on õige")
                                    print()
                                    ikoodid.append(ik)
                                elif 491<=int(ik[7:10])<=520:
                                    haigla="Järvamaa Haigla (Paide)"
                                    print("Isikukood on õige")
                                    print()
                                    ikoodid.append(ik)
                                elif 521<=int(ik[7:10])<=570:
                                    haigla="Rakvere, Tapa haigla"
                                    print("Isikukood on õige")
                                    print()
                                    ikoodid.append(ik)
                                elif 571<=int(ik[7:10])<=600:
                                    haigla="Valga Haigla"
                                    print("Isikukood on õige")
                                    print()
                                    ikoodid.append(ik)
                                elif 601<=int(ik[7:10])<=650:
                                    haigla="Viljandi Haigla"
                                    print("Isikukood on õige")
                                    print()
                                    ikoodid.append(ik)
                                elif 651<=int(ik[7:10])<=700:
                                    haigla="Lõuna-Eesti Haigla (Võru), Põlva Haigla"
                                    print("Isikukood on õige")
                                    print()
                                    ikoodid.append(ik)
                                else:
                                    print("Kahjuks isikukood on vale!")
                                    arvud.append(ik)
                                if ik[0] in ['1','2']:
                                    sunyear=1800+int(ik[1:3])
                                elif ik[0] in['3','4']:
                                    sunyear=1900+int(ik[1:3])
                                else:
                                    sunyear=2000+int(ik[1:3])
                                if ik[0] in naine:
                                    print(f"See on naine. Ta on sündinud {ik[5:7]}.{ik[3:5]}.{sunyear} ja sünnikoht on {haigla}")
                                    print()
                                    print()
                                if ik[0] in mees:
                                    print(f"See on mees. Ta on sündinud {ik[5:7]}.{ik[3:5]}.{sunyear} ja sünnikoht on {haigla}")
                                    print()
                                    print()
                            else:
                                print("Kahjuks isikukood on vale!")
                                arvud.append(ik)
                        else:
                            print("Sellist kuupäeva ei ole")
                            arvud.append(ik)
                    else:
                        print("Sellist kuud ei ole")
                        arvud.append(ik)
                else:
                    print("selline isikukood võib olla ainult tulevikus")
                    arvud.append(ik)
            else:
                print("Esimene sümbol ei ole õige")
                arvud.append(ik)
                print()
        else:
            print("Isikukoodis peab olema 11 märgi")
            arvud.append(ik)
            print()
        
        
        print(f"Õigete isikukoodide loetelu:\n{ikoodid}")  
        print()
        print()
        print(f"Valete isikokoodide loetel:\n{arvud}")
        print()
        print()
