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

