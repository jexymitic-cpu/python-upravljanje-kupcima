ime=input("Unesite ime radnika: ")
prezime=input("Unesite prezime radnika:")
broj_smena=int(input("Unesite broj smena u mesecu:"))
if broj_smena>3:
    print("Radnik ima vise od tri smena u mesecu.") 


elif broj_smena == 3:
    print("Radnik ima tacno tri smene u mesecu.")
else:
    print("Radnik ima manje od tri smene u mesecu.")
def broj_smena_U_mesecu(Ime,prezime,broj_smena):
    return Ime + " " + prezime + ",broj smena: " + str(broj_smena)
print(broj_smena_U_mesecu(ime, prezime, broj_smena))
radnici=["Dejan","Petar","Marko","Ema","Maja"]
radnici.append("Jelena")
print(len(radnici))
for radnik in radnici:
    print(radnik)
ukupno_radnih_sati=broj_smena*8
print("Ukupno radnih sati u mesecu:",ukupno_radnih_sati)
radnik1 = {
    "ime": "Dejan",
    "prezime": "Petrovic",
    "broj_smena": 20,
    "ukupno_sati": 20 * 8
}
radnik2= {
    "ime": "Petar",
    "prezime": "Nikolic",
    "broj_smena": 15,
    "ukupno_sati": 15 * 8
}
radnik3={
    "ime": "Marko",
    "prezime": "Jovanovic",
    "broj_smena": 10,
    "ukupno_sati": 10 * 8
}
radnik4={
    "ime": "Ema",
    "prezime": "Petrovic",
    "broj_smena":25,
    "ukupno_sati": 25*8
}
radnik5={
    "ime": "Maja",
    "prezime": "Nikolic",
    "broj_smena": 30,
    "ukupno_sati": 30 * 8
}
radnici=[radnik1,radnik2,radnik3,radnik4,radnik5]
for radnik in radnici:
    print("ime",radnik["ime"],"prezime",radnik["prezime"],"broj smena",radnik["broj_smena"],"ukupno",radnik["ukupno_sati"])