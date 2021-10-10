def czy_palindrom(tekst):
    for i in range(0, int(len(tekst) / 2)):
        if tekst[i] != tekst[len(tekst) - i - 1]:
            return False
    return True


tekst = str(input('podaj tekst'))

if (czy_palindrom(tekst)):
    print("jest palindromem")
else:
    print("nie jest palindromem")