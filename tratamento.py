def temAcento(texto):
    if "á" in texto or "à" in texto or "ã" in texto or "â" in texto or "é" in texto or "è" in texto or "ê" in texto  or "í" in texto or "ì" in texto or "î" in texto  or "ó" in texto or "ò" in texto or "õ" in texto or "ô" in texto  or "ú" in texto or "ù" in texto or "û" in texto or "ç" in texto:
        return True
    else:
        return False

def riscar(texto):
    return f'~~{texto}~~'

def sublinhar(texto):
    return f'__{texto}__'

def italico(texto):
    return f'*{texto}*'

def negrito(texto):
    return f'**{texto}**'