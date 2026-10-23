# Entradas
votos = int(input("¿Cuántos van a votar?: "))
print("Bandas")
print("1. Los borbotones")
print("2. Spinal Tap")
print("3. Los temerarios")

# Procesos

# Con while
voto = 1
while(voto <= votos):
    print(f"Voto {voto}. ", end="")
    seleccion = int(input("Introduce el voto: "))
    voto = voto + 1

# Con for
for v in range(1, votos + 1):
    print(f"Voto {v}. ")

# Salidas
