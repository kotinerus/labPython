dostep = {
    'piotrek1': 'porzeczka2',
    'basia13': 'zaq13edc',
    '_ananasek': 'spongebobd',
    'kamil124': 'wojtasszef',
    'pomidorowyziomek': 'cebula',
    'admin': 'admin'
}
login = str(input("Podaj login: "))
haslo = str(input("Podaj haslo: "))

if login in dostep:
    if(login==haslo=='admin'):
        print("Witaj na brzydkiej stronie")
    else:
        jakieHaslo = dostep[login]
        if(haslo==jakieHaslo):
            print("Witaj na stronie")
        else:
            print("Hasło niepoprawne. Odmowa dostępu")
else:
    print("Nie ma takiego użytkownika")

