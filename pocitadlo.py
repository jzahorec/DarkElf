rasy = ["Lide", "Barbari", "Skreti", "Skuruti", "Nekromanti", "Magove", "Elfove", "Temni Elfove", "Trpaslici", "Hobiti", "Enti"]
rasa = input("Zadej svoji rasu" + str(rasy) + ": ")
while rasa not in rasy:
    rasa = input("Zadej svoji rasu" + str(rasy) + ": ")
obyvatelstvo = int(input("Zadej pocet obyvatel: "))
domy = int(input("Zadej pocet domu: "))
vojaci_1 = int(input("Zadej pocet tvych obrannych(jednicek) v zemi: "))
vojaci_2 = int(input("Zadej pocet tvych utocnych(dvojek) v zemi: "))
vojaci_3 = int(input("Zadej pocet tvych magu(trojek) v zemi: "))
vojsko = [vojaci_1, vojaci_2, vojaci_3]
sypka = int(input("Kolik obyvatel mas za sypku(0 nebo 2): "))
porodnost = int(input("Zadej porodnost v %: "))
kola = int(input("Zadej pocet kol k odtahu: "))
pocasi_zlato = int(input("Zadej pocasi na zlato v %: "))
pocasi_mana = int(input("Zadej pocasi na manu v %: "))
pocasi_domy = int(input("Zadej pocasi na domy v %: "))

for kolo in range(kola):
    if int(((obyvatelstvo/20)+sypka+1)*(porodnost/100)+obyvatelstvo) + sum(vojsko[0:3]) > domy:
        print ("Domy jsou plné, od tahu " + str(kolo+1))
    else:
        obyvatelstvo = int(((obyvatelstvo/20)+sypka+1)*(porodnost/100)+obyvatelstvo)
    
print("Aktualni pocet obyvatel: " + str(obyvatelstvo))
verb = int(obyvatelstvo*0.8)
print ("Pocet obyvatel na verb: " + str(verb))
input("Konec programu")
