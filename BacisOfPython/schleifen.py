# Schleifen
einkaufsliste = ["apfel", "birne", "Milch"]

for item in einkaufsliste:
    print(item)
else:
    print("done")

for item in einkaufsliste:
    print(item)
    if item == "birne":
        break


for item in einkaufsliste:
    if item == "birne":
        continue
    print(item)

for x in range(5, 20):
    print(x)

for x in range(5, 20, 3):
    print(x)


# While lopps
i = 5
while i < 10:
    print(i)
    # i = i + 1
    i += i

# Nutzt man wenn break bedingung ist nicht von sequenz abhängt
while server_unavaiable:
    wait()
