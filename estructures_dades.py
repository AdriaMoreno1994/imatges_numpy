T1 = ["Gener", "Febrer", "Març"]
T2 = ["Abril", "Maig", "Juny"]
T3 = ["Juliol", "Agost", "Setembre"]
T4 = ["Octubre", "Novembre", "Decembre"]
trimestres = [T1, T2, T3, T4]

print("Ex1\n", trimestres)
print("\nEx 2\n")
print("El segon mes del primer trimestrer\n", trimestres[0][1])
print("Els mesos del primer trimestre\n", trimestres[0])

print("Ex2.3\n", trimestres[2][2], trimestres[3][0])

listaDesordenada = [3, 6, 4, 8, 6, 9, 3, 6, 5]
print("\nEx3\n")
print("Llista desordenada:\n", listaDesordenada)
print("nombre de vegades que apareix el 3:", listaDesordenada.count(3))

print("Nombre de vegades que apareix 3={0} i 4={1}".format(listaDesordenada.count(3), listaDesordenada.count(4)))
print("nombre més gran de la llista=", max(listaDesordenada))

llistaOrdenada = []
llistaOrdenada = listaDesordenada.copy()
llistaOrdenada.sort()

print("Els tres primers números més petits\n", llistaOrdenada[:3])

print("el rang de la llista es de {0} a {1}".format(min(listaDesordenada), max(listaDesordenada)))

print("\nEx 4\n")
compra = {
    "Pomes": {"Qty": 5, "€": 0.42},
    "Peres": {"Qty": 3, "€": 0.66}
}

compra["Llimona"] = {"Qty": 2, "€": 0.13}
print(compra)
preuPeres = compra["Peres"]["Qty"] * compra["Peres"]["€"]
print("Preu de les peres en total: ", preuPeres)
max_val = max(float(d["€"]) for d in compra.values())

for k, v in compra.items():
    if v["€"] == max_val:
        max_key = k

print("fruita més cara:", max_key)
