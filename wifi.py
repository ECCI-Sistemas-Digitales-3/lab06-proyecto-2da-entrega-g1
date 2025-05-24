import network
import time

SSID = 'POCO X6 Pro 5G'
PASSWORD = 'Jhonatan'

def conectar():
    # Crear el objeto de interfaz de red
    wifi = network.WLAN(network.STA_IF)
    wifi.active(True)

    # Conectarse si no está conectado
    if not wifi.isconnected():
        print('🔄 Conectando a la red WiFi...')
        wifi.connect(SSID, PASSWORD)

        # Esperar hasta que se conecte (con tiempo máximo de espera)
        timeout = 15  # Tiempo máximo de espera en segundos
        start = time.time()
        while not wifi.isconnected():
            if time.time() - start > timeout:
                print("⛔ No se pudo conectar al WiFi.")
                return False
            time.sleep(1)

    # Mostrar información de red si se conectó
    if wifi.isconnected():
        print("✅ Conectado a WiFi")
        print("Dirección IP:", wifi.ifconfig()[0])
        return True
    else:
        print("⚠️ Fallo al conectar.")
        return False

