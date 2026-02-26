def egalizare(a, b):
    #aducem la aceasi lungime sirurile
    max_len = max(len(a), len(b))
    return a.zfill(max_len), b.zfill(max_len)


def adunare(a, b):
    carry = 0
    resultat = ""
    a, b = egalizare(a,b)

    for i in range(len(a) - 1, -1, -1):
        s = carry + (a[i] == '1') + (b[i] == '1')
        if s % 2 == 1:
            resultat = "1" + resultat
        else:
            resultat = "0" + resultat
        if s > 1:
            carry = 1
        else:
            carry = 0
            
    if carry:
        resultat = "1" + resultat
    return resultat

def scadere(a, b):
    resultat = ""
    borrow = 0
    a, b = egalizare(a,b)

    for i in range(len(a) - 1, -1, -1):
        x = (a[i] == '1') - (b[i] == '1') - borrow
        if x >= 0:
            if x == 1:
                resultat = "1" + resultat
            else:
                resultat ="0" + resultat
            borrow = 0
        else:
            if x + 2 == 1:
                resultat = "1" + resultat
            else:
                resultat = "0" + resultat
            borrow = 1

    rezultat_final = resultat.lstrip("0")

    if rezultat_final == "":
        return "0"
    else:
        return rezultat_final



def inmultire(a, b):
    resultat = "0"
    shift = ""

    for i in range(len(b) - 1, -1, -1): 
        bit = b[i]
        if bit == "1":
            resultat = adunare(resultat, a + shift)
        shift += "0"

    return resultat


def impartire(a, b):
    rezultat = ""
    aux = "0"

    for i in range(0, len(a)): 
        bit = a[i]
        aux = scadere(aux + bit, "0")
        if scadere(aux, b) != "0" and not scadere(aux, b).startswith("-"):
            aux = scadere(aux, b)
            rezultat += "1"
        else:
            rezultat += "0"

    rezultat_final = rezultat.lstrip("0")
    
    if rezultat_final == "":
        return "0"
    else:
        return rezultat_final



# Exemple
print("Adunare:", adunare("1011", "110"))
print("Scadere:", scadere("1011", "110"))
print("Inmultire:", inmultire("1011", "110"))
print("Impartire:", impartire("1011", "110"))