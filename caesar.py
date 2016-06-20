def int2ascii(i):
    c = chr(i)
    return c

def ascii2int(c):
    i = ord(c)
    return i

def caesarVerschluesselungBuchstabe( klartextbuchstabe ):
    zahl = ascii2int( klartextbuchstabe )
    verschluesselteZahl= zahl + 3
    if (verschluesselteZahl >= 91):
        verschluesselteZahl = verschluesselteZahl - 26
    # print zahl
    # print verschluesselteZahl
    verschluesselterBuchstabe = int2ascii( verschluesselteZahl )
    return verschluesselterBuchstabe

def caesarEntschluesselungBuchstabe( geheimtextbuchstabe ):
    zahl = ascii2int( geheimtextbuchstabe )
    entschluesselteZahl= zahl - 3
    if (entschluesselteZahl <=64):
        entschluesselteZahl = entschluesselteZahl + 26
    # print zahl
    # print verschluesselteZahl
    entschluesselterBuchstabe = int2ascii( entschluesselteZahl )
    return entschluesselterBuchstabe

def caesarVerschluesselung( klartext ):
    geheimtext = ""
    for char in klartext:
        geheimtext = geheimtext + caesarVerschluesselungBuchstabe( char )
    return geheimtext

def caesarEntschluesselung( geheimtext ):
    klartext = ""
    for char in geheimtext:
        klartext = klartext + caesarEntschluesselungBuchstabe( char )
    return klartext

def deleteSpaces(text):
    textOhneLeerzeichen = ""
    for char in text:
        if char != ' ':
            textOhneLeerzeichen = textOhneLeerzeichen + char
    return textOhneLeerzeichen


modus = raw_input("Moechtest du (e)ntschluesseln oder (v)erschluesseln: ")
if (modus=="v"):
    print"Modus: Verschluesseln"
    klartext = raw_input("Gib einen Klartext ein: ")
    klartextOhneLeerzeichen = deleteSpaces( klartext )
    print "Klartext ohne Leerzeichen: " + klartextOhneLeerzeichen
    geheimtext = caesarVerschluesselung( klartextOhneLeerzeichen )
    print "Der Geheimtext lautet:     " + geheimtext
    #klartextNeu = caesarEntschluesselung( geheimtext )
    #print "Der KlartextNeu lautet:    " + klartextNeu

if (modus=="e"):
    print "Modus: Entschluesseln"
    geheimtext = raw_input("Gib einen Geheimtext ein: ")
    klartext = caesarEntschluesselung( geheimtext )
    #print "Der Geheimtext lautet:     " + geheimtext
    print "Der Klartext lautet:      " + klartext
