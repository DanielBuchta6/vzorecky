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
