print("Vítejte v aplikaci pro výpočet obsahu kruhu: ")

r = input("Zadejte poloměr kruhu: ")

r = int(r)
π = int(3.14)

if r>0:
    print("vysledek je: ")
    print(π *(r*r ))
    
else:
    print("co pak to děláš ? však jsi zadal záporné číslo")
    