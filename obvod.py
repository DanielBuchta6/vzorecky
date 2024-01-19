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