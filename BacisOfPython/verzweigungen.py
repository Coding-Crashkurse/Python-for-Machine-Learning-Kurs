# Verzweigungen (if, else, elif) / Indentation

if 2 > 1 == True:
    print("größer")

if 2 > 1:
    print("größer")

if 2 > 1:
    print("größer")
else:
    print("nicht größer")

x = 3

if x > 4:
    print("größer 4")
elif x > 5:
    print("größer 5")
else:
    print("kleiner als 4")

####################################

x = 6

if x > 5:
    print("größer 5")
elif x > 4:
    print("größer 4")
else:
    print("kleiner als 4")


x = 6

if x > 5:
    print("größer 5")
elif x < 5 and x > 3:
    print("kleiner als 5 und größer als 3")
else:
    print("kleiner als 3")
