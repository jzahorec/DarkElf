obyvatelstvo = int(input("Zadej pocet obyvatel: "))
sypka = int(input("Kolik obyvatel mas za sypku(0 nebo 2): "))
porodnost = int(input("Zadej porodnost v %: "))
kola = int(input("Zadej pocet kol k odtahu: "))

for kolo in range(kola):
    obyvatelstvo = int(((obyvatelstvo/20)+sypka+1)*(porodnost/100)+obyvatelstvo)
    
print(obyvatelstvo)
verb = int(obyvatelstvo*0.8)
print (verb)
