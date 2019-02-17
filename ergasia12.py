import os
from collections import OrderedDict

f = open("paradeigma.txt", "r")
input_str = f.read()
syxnothta = {}
#syxnothta xarakthrwn
for i in input_str: 
    if i in syxnothta: 
        syxnothta[i] += 1
    else: 
        syxnothta[i] = 1
#ektypwse syxnothta
lista_descend = []
lista_ascend = []
syxn_sort_1 = [(key, syxnothta[key]) for key in sorted(syxnothta, key=syxnothta.get, reverse=True)]
for key, value in syxn_sort_1:
    lista_descend.append(str(key))
    print("xaraktiras='"+str(key)+"' syxnothta="+str(value))
syxn_sort_2 = [(key, syxnothta[key]) for key in sorted(syxnothta, key=syxnothta.get, reverse=False)]
for key, value in syxn_sort_2:
    lista_ascend.append(str(key))

print("\n")

s= list(input_str)
ind = 0
#antikatastash
for i in input_str:
    for j in range(0,len(lista_descend)):
        if i == lista_descend[j]:
            s[ind] = lista_ascend[j]
            break
    ind += 1

final_string = "".join(s)
#ejodos se kefalaia
print (final_string.upper())	

