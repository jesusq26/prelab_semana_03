print("A. Mover a la derecha")
print("B. Mover a la izquierda")
print("C. Mover hacia el frente")
print("D. Mover hacia atrás")
print("E. Apagar")

while True:
    opcion = input("Seleccione una opción (A, B, C, D, E): ")

    if opcion == "A":
        print("El robot se desplazó a la derecha.")
    elif opcion == "B":
        print("El robot se desplazó a la izquierda.")
    elif opcion == "C":
        print("El robot se desplazó hacia el frente.")
    elif opcion == "D":
        print("El robot se desplazó hacia atrás.")
    elif opcion == "E":
        print("Apagando el sistema...")
        break
    else:
        print("Comando no reconocido. Intente de nuevo.")

