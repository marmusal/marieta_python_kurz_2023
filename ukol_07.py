class Auto: 
    def __init__(self, registracni_znacka, typ_vozidla, najete_km, dostupne): 
        self.registracni_znacka = registracni_znacka
        self.typ_vozidla = typ_vozidla
        self.najete_km = najete_km
        self.dostupne = True


    def pujc_auto(self): 
        if self.dostupne :

            self.dostupne = False
            return f"Automobil {self.typ_vozidla} je vám k dispozici, potvrzuji zapůjčení vozidla! "
        
        else:
            return f"Automobil {self.typ_vozidla} bohužel není k dispozici. "
        
    def get_info(self):
        return f"Automobil {self.typ_vozidla} s registrační značkou {self.registracni_znacka} má najeto {self.najete_km}. "


peugeot = Auto("4A2 3020" , "Peugeot 403 Cabrio" , 47534 , True)
skoda = Auto("1P3 4747" , "Škoda Octavia" , 41253 , True)

volba = input("Jakou značku si přejete půjčit? (peugeot/skoda): ")


if volba == "peugeot":
    print(peugeot.get_info())
    print(peugeot.pujc_auto())
elif volba == "skoda":
    print(skoda.get_info())
    print(skoda.pujc_auto())
else:
    print("Neplatná volba značky.")



