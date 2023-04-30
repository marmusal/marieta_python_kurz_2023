'''Uvažuj, že píšeš jednoduchou aplikaci pro zasílání SMS zpráv. Napiš program, který provede následující činnosti:

Zeptá se uživatele na číslo, kam chce zprávu zaslat a ověří, že číslo má správný formát.
Zeptá se uživatele na zprávu, kterou chce zaslat. Následně vypíše, kolik zpráva bude stát.
Tvůj program bude obsahovat dvě funkce:

První funkce ověří telefonní číslo. Uvažuj, že telefonní číslo může být devítimístné nebo třináctimístné (pokud je na začátku předvolba "+420"). Funkce ověří, jestli je číslo platné. Pokud je platné, vrátí hodnotu True, jinak vrátí hodnotu False.
Druhá funkce spočte cenu zprávy. Uživatel platí 3 Kč za každých započatých 180 znaků.
Tvůj program nejprve ověří pomocí první funkce správnost telefonního čísla. Pokud není platné, vypíše chybu, v opačném případě se zeptá na text zprávy a pomocí druhé funkce určí její cenu, kterou vypíše uživateli.

Tipy:

Nemusíte kontrolovat, zda uživatel zadal skutečně číslo, či zda jsou tam i jiné znaky. To jsme v kurzu zatím neřešili.
Pro kontrolu předvolby použijte slicing (viz první lekce) pro získání prvních 4 znaků řetězce. Ty porovnejte s řetězcem "+420".'''

import math

tel_cislo = input("Zadejte prosím telefonní číslo pro zaslání SMS ve tvaru +420xxxxxxxxx : ")
predvolba = (tel_cislo[0:4])
predvolba_str = str(predvolba)

if predvolba_str != ('+420'):
    print("Telefonní číslo není ve správném tvaru. Spusťte zadáváni odznovu! ")    
else:
    print("Telefonní číslo ověřeno. ")

    text_zpravy = input("Zadejte prosím text zprávy: ")
    pocet_znaku = len(text_zpravy)

    pocet_zprav = math.ceil(pocet_znaku/180)
    cena_sms = pocet_zprav*3
    print("Cena Vaší SMS zprávy bude" , cena_sms , "Kč! ")




