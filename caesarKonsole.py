import sys

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

def caesarVerschluesselung(klartext):
    geheimtext = ""
    for char in klartext:
        geheimtext = geheimtext + caesarVerschluesselungBuchstabe( char )
    return geheimtext

def deleteSpaces(text):
    textOhneLeerzeichen = ""
    for char in text:
        if char != ' ':
            textOhneLeerzeichen = textOhneLeerzeichen + char
    return textOhneLeerzeichen

# use stdin if it's full                                                        
if not sys.stdin.isatty():
    input_stream = sys.stdin

# otherwise, read the given filename                                            
else:
    try:
        input_filename = sys.argv[1]
    except IndexError:
        message = 'need filename as first argument if stdin is not full'
        raise IndexError(message)
    else:
        input_stream = open(input_filename, 'rU')

for klartext in input_stream:
    print klartext # do something useful with each line
    
    #klartext = raw_input("Gib einen Klartext ein: ")
    #lartext = str(sys.argv[1]);
    klartextOhneLeerzeichen = deleteSpaces( klartext )
    print "Klartext ohne Leerzeichen: " + klartextOhneLeerzeichen
    geheimtext = caesarVerschluesselung( klartextOhneLeerzeichen )
    print "Der Geheimtext lautet:     " + geheimtext
    #print "Der Klartext lautet:      " + klartext
