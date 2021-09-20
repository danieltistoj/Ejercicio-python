disMe = input("Metro recorridos: ")
timMi = input("Minutos empleados: ")

disKm = float(disMe) / 1000
timHo = float(timMi) / 60
velocidad = disKm / timHo

#velocidad = (float(input("Metro recorridos: ")) / 1000) / (float(input("Minutos empleados: ")) / 60)

if(velocidad > 75):
    print(f"La velocidad de {velocidad:1.2f} Km/h es Alta")
elif(velocidad < 30):
    print(f"La velocidad de {velocidad:1.2f} Km/h es Baja")
else:
    print(f"La velocidad de {velocidad:1.2f} Km/h es Moderada")