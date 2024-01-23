#obvod obdelníku
print("Vítejute v aplikaci pro výpočet obvodu obdelníku")

a = input("Zadejte délku strany a: ")
b = input("Zadejte délku strany b: ")

a = int(a)
b = int(b)

if a>0 and b>0:
    print("vysledek je: ")
    print(2*a+2*b)

else:
    print("co pak to děláš ? však jsi zadal záporné číslo")

#obsah obdelníku 
print("Vítejte v aplikaci pro výpočet obsahu obdelníku")

a = input("Zadejte délku strany a: ")
b = input("Zadejte délku strany b: ")

a = int(a)
b = int(b)

if a>0 and b>0:
    print("vysledek je: ")
    print(a*b)

else:
    print("co pak to děláš ? však jsi zadal záporné číslo")
    
#obsah kruhu
print("Vítejte v aplikaci pro výpočet obsahu kruhu: ")

r = input("Zadejte poloměr kruhu: ")

r = int(r)
π = int(3.14)

if r>0:
    print("vysledek je: ")
    print(π *(r*r ))
    
else:
    print("co pak to děláš ? však jsi zadal záporné číslo")
    
#objem kvadru
print("Vítejte v aplika pro výpočet objemu kvadru: ")

a = input("Zadejte délku hrany a : ")
b = input("Zadejte délku hrany b : ")
c = input("Zadejte délku hrany c : ")

a = int(a)
b = int(b)
c = int(c)

if a>0 and b>0 and c>0:
    print("vysledek je: ")
    print(a*b*c)
    
else:
    print("co pak to děláš ? však si zadal záporné číslo")
    
#výběr 
while:
    print("vyberte co chcete počítat: ")
    print("vyberte 1 pro výpočet obvodu obdelníku: ")
    print("vyberte 2 pro výpočet obsahu obdelníku: ")
    print("vyberte 3 pro výpočet obsahu kruhu: ")
    print("vyberte 4 pro výpočet objemu kvádru: ")
    
    
    
    