def  remove_duplicates(txt: str) -> str:
    if len(txt) == 1:
        return txt
    if txt[0] == txt[1]:
        return remove_duplicates(txt[1:])
    return txt[0] + remove_duplicates(txt[1:])

print(remove_duplicates("xxyyyzz"))