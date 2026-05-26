voti=["1","2","3","4"]

voti.append("8")

for p in voti:
    print("Voto registrato:")
    print(p)

print("Voti terminati")

print("elimino voto: " + voti.pop())

voti.insert(2,5)

for p in voti:
    print(p)