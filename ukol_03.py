import json

with open('body.json', encoding='utf-8') as file:
    data = json.load(file)


prospech = {}
for jmeno, body in data.items():
    if body >= 60:
        prospech[jmeno] = "Pass"
    else:
        prospech[jmeno] = "Fail"



with open('prospech.json', 'w') as file:
    json.dump(prospech, file, sort_keys=True, indent=4, separators=(',', ': '))


# Z nějakého důvodu mám problém s výpisem diakritiky ve výsledném json souboru. Jak to prosím můžu vyřešit?