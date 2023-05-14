kontakty = {
    'Mikołaj':603413412,
    'Hogwart':605475696,
    'Kapitan Ameryka':678136709,
    'Piotrek':605475696,
    'Józek':555675328,
    'Szwed':771793336,
    'Krystian':892345612,
    'Ania':928401426,
    'Basia':917462112,
    'Kasia':980132756
}
kontakty['Amelia']=kontakty.pop('Mikołaj')
kontakty['Borys'] = kontakty.pop('Kasia')
print(kontakty)
kontakty.clear()
print(kontakty)
kontakty["Patrycja"] = 701234587
kontakty["Dawid"] = 617823109



#SORTOWANIE PO NAZWIE
print(sorted(kontakty.items()))
print(list(sorted(kontakty.items())))