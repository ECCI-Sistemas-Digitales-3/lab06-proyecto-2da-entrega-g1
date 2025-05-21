[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=19409293&assignment_repo_type=AssignmentRepo)
# Lab06: Proyecto 2da. entrega

## Integrantes

[Jhonatan Rodriguez Grisales](https://github.com/Jhonatan-3011)


[Nelson Prada](https://github.com/nelson18prada)

[Miguel Angel Bernal](https://github.com/Miguelbernalradio) 

## Documentación

### Version 2.0

En el archivo [lectura_ultrasonido.py](/lectura_ultrasonido.py) se encuentra el script donde se implementa la lectura de datos desde dos sensores ultrasónicos conectados a una Raspberry Pi mediante la biblioteca gpiozero. Cada sensor se configura con un par de pines GPIO para la señal de disparo (trigger) y la señal de eco (echo), y se les otorga un tiempo breve de estabilización antes de comenzar la lectura. El sistema convierte la distancia medida por los sensores (originalmente en metros) a centímetros, y luego la restringe dentro de un rango útil definido entre 2 cm (indica lleno) y 15 cm (indica vacío), eliminando valores extremos que puedan distorsionar la medición.

La lógica principal del código incluye una función que calcula el porcentaje de llenado del contenedor basado en la distancia leída. Este cálculo se realiza mediante una regla de tres inversa, considerando que a menor distancia corresponde un mayor porcentaje de llenado. El resultado es formateado con dos decimales de precisión y se limita para asegurar que siempre se mantenga entre 0% y 100%. Para mejorar la legibilidad y adaptación del código, la función leer_sensor() centraliza esta operación y se reutiliza para ambos sensores.

Finalmente, el sistema muestra en consola únicamente el porcentaje de llenado de cada sensor, Además, el porcentaje se guarda en archivos de texto individuales para cada sensor, lo que facilita su posterior consulta o integración con otros sistemas. Las líneas relacionadas con la impresión y almacenamiento de la distancia original han sido comentadas intencionalmente, siguiendo un requerimiento específico, sin eliminar la funcionalidad subyacente para posibles usos futuros.

### Version 2.1

En el archivo [lectura_ultrasonido_esp32.py](/lectura_ultrasonido_esp32.py) se desarrolló un sistema de monitoreo de nivel de líquido basado en sensores ultrasónicos HC-SR04 conectados a una placa ESP32. El objetivo fue medir la distancia entre la superficie del líquido y el sensor, para luego calcular un porcentaje de llenado. La medición se realiza mediante pulsos ultrasónicos que permiten conocer el tiempo de ida y vuelta del sonido, lo cual se convierte en distancia en centímetros. Esta información es útil en sistemas de control donde se requiere conocer el nivel de líquidos en este caso de la pintura en cada envace.

La ESP32 fue programada en MicroPython desde el entorno Thonny, lo que facilitó una programación modular y eficiente. Se configuraron cinco sensores ultrasónicos, cada uno con sus pines TRIG y ECHO definidos, y se desarrolló una función leer_distancia() encargada de gestionar las señales de activación del sensor y de medir el tiempo del eco usando time_pulse_us(). Se añadieron validaciones para descartar lecturas fuera de rango o errores de tiempo de espera, asegurando mayor confiabilidad en los datos obtenidos.

Una vez medida la distancia, se implementó la función calcular_porcentaje() que convierte dicha distancia en un porcentaje relativo al rango útil de medición (entre 2.0 cm y 15.0 cm). Este valor porcentual representa el nivel del depósito en términos comprensibles y normalizados. De esta manera, se obtiene una interpretación más intuitiva de los datos del sensor, útil para ser visualizada en interfaces como lo es en nuestro caso por medio de Node-RED

Para habilitar la conectividad, se creó un módulo externo wifi.py que permite conectar la ESP32 a una red Wi-Fi local. Una vez establecida la conexión, se configura un cliente MQTT usando la librería umqtt.simple, estableciendo comunicación con el broker definido por la IP de una Raspberry Pi. Esta configuración incluye el puerto, un identificador único del cliente (esp32_sensor) y el tópico MQTT sensores/ultrasonico, al cual la ESP32 publica los datos.

El broker MQTT corre en una Raspberry Pi, utilizando Mosquitto como servidor MQTT. Este broker recibe los mensajes publicados por la ESP32, permitiendo que otros clientes MQTT se suscriban a ese mismo tópico para recibir en tiempo real las lecturas del nivel. Esta arquitectura descentralizada permite escalar el sistema fácilmente, ya sea integrando nuevos sensores o desarrollando dashboards en otros dispositivos suscritos.

En el bucle principal del script, la ESP32 itera sobre los cinco sensores definidos, lee sus distancias, calcula los porcentajes correspondientes y los publica al tópico MQTT en intervalos regulares de tres segundos. Se incorporó manejo de errores para la publicación de datos, lo cual mejora la estabilidad del sistema ante fallos de red o desconexiones temporales. Además, los mensajes enviados incluyen el número de sensor y su porcentaje de llenado, facilitando su identificación y seguimiento.

En conclusion, este sistema integra hardware y software de forma eficaz para el monitoreo remoto de niveles de líquido. Se utilizan tecnologías abiertas como MicroPython, MQTT y Mosquitto, lo que garantiza flexibilidad, bajo consumo de recursos y facilidad de implementación. Este proyecto es una base sólida para aplicaciones más complejas de IoT, como alertas por bajo nivel y visualización en dashboards entre otras.

## Metodologia

Se realiza la conexion entre la raspberry pi y los sensores ultrasonido. 

![conexion_raspberry_ultrasonidos](/conexion_raspberry_ultrasonidos.jpeg)

ahora realizamos la conexion entre la esp32 y los sensores ultrasonido, y la raspberry pi la usamos como broker.

![conexion_esp32_ultrasonidos](/circuito_completo.jpeg)

Luego se realiza la lectura por medio de python.

![lectura_python.png](/lectura_python.png)

por medio de Thonny visualizamos los datos recibido en la esp32

![lectura_thonny.png](/lectura_thonny.png)

observamos los valores en node-RED.

![lectura_node_red](/lectura_node_red.png)

 se acomoda la interface en node red y se le adicionan unos leds.

![lectura_node](/lectura_node.png)

## diagrama de flujo 

![Diagrama de flujo](/diagrama%20de%20flujo.png)