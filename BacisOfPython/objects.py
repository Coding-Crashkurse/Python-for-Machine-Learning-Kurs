# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 19:38:02 2020

@author: User
"""


isinstance(1.2, object)

# Objects haben Attribute und Methoden

"test".__len__()
"test".capitalize()
[].append(1)

x = [1, 2, 3, 4, 5]
result = []

for zahl in x:
    if zahl > 3:
        zahl = zahl / 2
        result.append(zahl)
    else:
        result.append(zahl)

print(result)

