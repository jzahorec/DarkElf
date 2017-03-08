rasy = {"Lide":[[1,5],[7,3],[4,4]], "Barbari":[[4,3],[9,3],[5,4]], "Skreti":[[2,4],[5,3],[3,3]], "Skuruti":[[3,3],[7,1],[5,3]], "Nekromanti":[[1,4],[7,2],[5,3]], "Magove":
[[2,5],[7,2],[3,5]], "Elfove":[[2,6],[6,4],[5,5]], "Temni Elfove":[[3,5],[8,3],[4,5]], "Trpaslici":[[2,7],[5,6],[3,7]], "Hobiti":[[2,2],[4,2],[1,2]], "Enti":[[4,6],[8,8],[3,6]]}

vypis_ras = " ("
toceni = 0
for i in rasy:
    toceni += 1
    if toceni < len(rasy):
        vypis_ras += i+", "
    else:
        vypis_ras += i + ")"
rasa = input("Zadej svoji rasu" + str(vypis_ras) + ": ")
while rasa not in rasy:
    rasa = input("Zadej svoji rasu" + str(vypis_ras) + ": ")

verb_koef = 0.2
if rasa == "Enti":
	verb_koef = 0.1

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
verb = int(obyvatelstvo - domy*verb_koef)
if verb < 0:
	verb = 0
print ("Pocet obyvatel na verb: " + str(verb))
input("Konec programu")
