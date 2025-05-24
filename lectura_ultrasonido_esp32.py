from machine import Pin, time_pulse_us
import time
import wifi  # conecta a WiFi
from umqtt.simple import MQTTClient

# === Configuración de WiFi ===
wifi.conectar()  # archivo como wifi.py

# === Configuración MQTT ===
MQTT_BROKER = "192.168.166.46"  # Reemplaza con la IP de tu Raspberry Pi
MQTT_PORT = 1883
MQTT_CLIENT_ID = "esp32_sensor"
MQTT_TOPIC = b"sensores/ultrasonico"

client = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER, port=MQTT_PORT)
client.connect()

# === Configuración de pines para ESP32 ===
SENSORES = [
    {"trig": 2, "echo": 18},
    {"trig": 4, "echo": 19},
    {"trig": 5, "echo": 21},
]

# === Parámetros del sensor ===
DISTANCIA_MINIMA_CM = 2.0
DISTANCIA_MAXIMA_CM = 15.0
RANGO_UTIL = DISTANCIA_MAXIMA_CM - DISTANCIA_MINIMA_CM
INTERVALO_LECTURA = 3  # Intervalo entre lecturas en segundos

def leer_distancia(sensor):
    trig = Pin(sensor["trig"], Pin.OUT)
    echo = Pin(sensor["echo"], Pin.IN)

    trig.value(0)
    time.sleep_us(5)
    trig.value(1)
    time.sleep_us(10)
    trig.value(0)

    try:
        duracion = time_pulse_us(echo, 1, 30000)
    except OSError as e:
        print(f"⚠️ Error de tiempo de espera en el sensor {sensor['trig']} - {e}")
        return None

    if duracion <= 0 or duracion > 30000:
        print(f"⚠️ Duración fuera de rango en el sensor {sensor['trig']}: {duracion} us")
        return None

    distancia_cm = (duracion / 2) / 29.1
    return distancia_cm

def calcular_porcentaje(distancia_cm):
    if distancia_cm is None:
        return 0.00
    distancia_cm = max(DISTANCIA_MINIMA_CM, min(distancia_cm, DISTANCIA_MAXIMA_CM))
    porcentaje = ((DISTANCIA_MAXIMA_CM - distancia_cm) / RANGO_UTIL) * 100
    return round(porcentaje, 2)

# === Bucle infinito de lectura y envío por MQTT ===
while True:
    for i, sensor in enumerate(SENSORES):
        distancia = leer_distancia(sensor)
        porcentaje = calcular_porcentaje(distancia)
        mensaje = f"Sensor {i+1}: {porcentaje:.2f} %"
        print(mensaje)

        try:
            client.publish(MQTT_TOPIC, mensaje)
        except Exception as e:
            print(f"⚠️ Error al enviar MQTT: {e}")

    time.sleep(INTERVALO_LECTURA)