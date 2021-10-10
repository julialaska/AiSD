def foo(imie,nazwisko):
    imie = imie[0].upper()
    nazwisko = nazwisko.title()
    return imie + '.' + nazwisko

def foo2(imie, nazwisko,foo):
    return foo(imie, nazwisko)

print(foo2('jan','kowalski',foo))