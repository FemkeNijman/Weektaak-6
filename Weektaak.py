def lees_bestand(bestandsnaam):
    bestand = open(bestandsnaam)
    lijst = []
    for i in bestand:
        lijst.append(i.strip().split("\t"))
    return lijst

def filteren(lijst):
    gefilterde_lijst = []
    try:
        for i in lijst:
            if i[31] == "FALSE":
                if i[10] == "":
                    if int(i[6]) >= 5:
                        if int(i[7]) >= 20:
                            if i[22] != "INTRON_REGION" and i[22] != "" and i[22] != "UTR":
                                gefilterde_lijst.append(i)

    except IndexError:
        pass
    return gefilterde_lijst

def hgmd_filter(lijst, gefilterde_lijst):
    try:
        for i in lijst:
            if "HGMD" in i[51]:
                gefilterde_lijst.append(i)
    except IndexError:
        pass
    return gefilterde_lijst

def main():
    bestandsnaam = "21213_hcdiffs.txt"
    lijst = lees_bestand(bestandsnaam)
    gefilterde_lijst = filteren(lijst)
    gefilterde_lijst = hgmd_filter(lijst, gefilterde_lijst)
    print(gefilterde_lijst)
    print(len(gefilterde_lijst))
main()