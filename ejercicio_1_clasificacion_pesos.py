pesos_piezas = [12.5, -5.0, 14.2, 0.0, 18.1, 10.5]
countL = 0
countP = 0
count = 0

for i in range(len(pesos_piezas)):
    if pesos_piezas[i] <= 0:
        print("Error de lectura: Flujo negativo descartado.")
    elif pesos_piezas[i] >= 1 and pesos_piezas[i] <= 13:
        print("Pieza Ligera aprobada.")
        countL += 1
    elif pesos_piezas[i] > 13:
        print("Pieza Pesada aprobada.")
        countP += 1
count = countL + countP

print(f"Total de piezas ligeras aprobadas: {countL}")
print(f"Total de piezas pesadas aprobadas: {countP}")
print(f"Total de piezas aprobadas: {count}")