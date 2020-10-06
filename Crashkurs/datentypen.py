### Datentypen ###

# Strings (str)
'einfache Anführungszeichen'
"doppelte Anführungszeichen"
'Ich bin "nested"'

string = "test"
# Numeric (int, float)
x = 3
y = 3.2
z = x + y
type(z)

# Sequence types (list, tuple, set, string) mutability
einkaufsliste = ["apfel", "birne", "Milch"]
einkaufsliste[0]
einskausliste = ["Apfel", ["Milch", "Schokolade"]]
einskausliste[1][0]

einkaufsliste[0:2]
einkaufsliste[-1]
einkaufsliste[-1] = "H-Milch"
einkaufsliste

gemischte_liste = [1, 2, "test"]
einkaufstupel = ("apfel", "birne", "Milch", "birne")
einkaufstupel[1] = "Pfirsisch"

einkaufsset = {"apfel", "birne", "Milch", "birne"}
einkaufsset[1] = "Pfirsisch"
string = "test"
string[1] = "a"

# Mapping types (dict)
einkaufsdictionary = {"Milch": 0.99, "Apfel": 0.6}
einkaufsdictionary["Milch"]

# Booleans (bool)
True
False
