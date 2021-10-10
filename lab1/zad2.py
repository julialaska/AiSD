def foo(imie,nazwisko):
    imie = imie[0].upper()
    nazwisko = nazwisko.title()
    return imie + '.' + nazwisko

print(foo('jan','kowalski'))