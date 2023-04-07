# HLAVNÍ ÚKOL

sklad = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}

#  Software se nejprve zeptá na kód součástky a poté na množství, které si zákazník chce koupit. Obě informace si ulož. 
kod = input("Zadejte kód součástky: ")
mnozstvi = int(input("Zadejte požadované množství: "))

if kod in sklad:
    if sklad[kod] == 0:
            print("Součástka s kódem", kod, "není skladem.")

    elif sklad[kod] < mnozstvi:
            print("Lze prodat pouze", sklad[kod], "kusů součástky s kódem", kod + ".")
            souhlas = input("Je to pro vás v pořádku? Napište, prosím, ano/ne  ")
            if souhlas == "ano":
                print("Díky, objednávka vyřízena. ")
                sklad.pop(kod)
            else:
                  print("Zkuste se zeptat příští týden, nashledanou. ")
                  
    else:
            print("Poptávku lze uspokojit v plné výši.")
            sklad[kod] -= mnozstvi

else:
    print("Součástka s kódem", kod, "není skladem.")



# NEPOVINNÝ 01

morse_code = {
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "!": "-.-.--",
    "-": "-....-",
    "/": "-..-.",
    "@": ".--.-.",
    "(": "-.--.",
    ")": "-.--.-",
}

# dotaz na text
text = input("Zadej text pro přepis do Morseovy abecedy malými písmeny a bez diakritiky: ")

#úvod
print("Váš text v Morseově abecedě vypadá takto: ")
# procházení 
for char in text:
    # je znak mezera?
    if char == " ":
        # mezera je lomítko
        print("/", end=" ")
    else:
        # hledám ve slovníku
        # a vypíši překlad
        print(morse_code.get(char.lower(), ""), end=" ")