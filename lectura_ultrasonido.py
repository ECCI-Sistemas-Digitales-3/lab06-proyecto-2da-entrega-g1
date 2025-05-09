#lectura en porcentaje de 2 sensores

from gpiozero import DistanceSensor
from time import sleep

# === Configura los sensores ===
sensor1 = DistanceSensor(echo=24, trigger=23)
sensor2 = DistanceSensor(echo=27, trigger=17)

# Espera a que los sensores se estabilicen
sleep(1)

# === Límites de medición útiles (aplicados a ambos sensores) ===
distancia_minima_cm = 2.0    # Lleno
distancia_maxima_cm = 15.0   # Vacío
rango_util = distancia_maxima_cm - distancia_minima_cm

# === Función para obtener distancia y porcentaje de llenado ===
def leer_sensor(sensor):
    distancia_cm = sensor.distance * 100
    distancia_cm = max(distancia_minima_cm, min(distancia_cm, distancia_maxima_cm))
    porcentaje = ((distancia_maxima_cm - distancia_cm) / rango_util) * 100
    porcentaje = max(0.0, min(porcentaje, 100.0))
    return distancia_cm, porcentaje

# === Lectura del Sensor 1 ===
distancia1, porcentaje1 = leer_sensor(sensor1)
distancia1_formateada = f"{distancia1:.2f} cm"
porcentaje1_formateado = f"{porcentaje1:.2f} %"
# print(f"[Sensor 1] Distancia: {distancia1_formateada}")  # Comentado: no mostrar distancia
print(f"[Sensor 1] Porcentaje de llenado: {porcentaje1_formateado}")

# Guarda los resultados del sensor 1
ruta_sensor1 = "/home/pi/Documents/sistemas_digitales3/lectura_distancia_1.txt"
with open(ruta_sensor1, "w") as archivo1:
    # archivo1.write(f"Distancia: {distancia1_formateada}\n")  # Comentado: no guardar distancia
    archivo1.write(f"Llenado: {porcentaje1_formateado}\n")

# === Lectura del Sensor 2 ===
distancia2, porcentaje2 = leer_sensor(sensor2)
distancia2_formateada = f"{distancia2:.2f} cm"
porcentaje2_formateado = f"{porcentaje2:.2f} %"
# print(f"[Sensor 2] Distancia: {distancia2_formateada}")  # Comentado: no mostrar distancia
print(f"[Sensor 2] Porcentaje de llenado: {porcentaje2_formateado}")

# Guarda los resultados del sensor 2
ruta_sensor2 = "/home/pi/Documents/sistemas_digitales3/lectura_distancia_2.txt"
with open(ruta_sensor2, "w") as archivo2:
    # archivo2.write(f"Distancia: {distancia2_formateada}\n")  # Comentado: no guardar distancia
    archivo2.write(f"Llenado: {porcentaje2_formateado}\n")