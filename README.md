[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=19409293&assignment_repo_type=AssignmentRepo)
# Lab06: Proyecto 2da. entrega

## Integrantes

[Jhonatan Rodriguez Grisales](https://github.com/Jhonatan-3011)


[Nelson Prada](https://github.com/nelson18prada)

[Miguel Angel Bernal](https://github.com/Miguelbernalradio) 

## Documentación

En el archivo [lectura_ultrasonido.py](/lectura_ultrasonido.py) se encuentra el script donde se implementa la lectura de datos desde dos sensores ultrasónicos conectados a una Raspberry Pi mediante la biblioteca gpiozero. Cada sensor se configura con un par de pines GPIO para la señal de disparo (trigger) y la señal de eco (echo), y se les otorga un tiempo breve de estabilización antes de comenzar la lectura. El sistema convierte la distancia medida por los sensores (originalmente en metros) a centímetros, y luego la restringe dentro de un rango útil definido entre 2 cm (indica lleno) y 15 cm (indica vacío), eliminando valores extremos que puedan distorsionar la medición.

La lógica principal del código incluye una función que calcula el porcentaje de llenado del contenedor basado en la distancia leída. Este cálculo se realiza mediante una regla de tres inversa, considerando que a menor distancia corresponde un mayor porcentaje de llenado. El resultado es formateado con dos decimales de precisión y se limita para asegurar que siempre se mantenga entre 0% y 100%. Para mejorar la legibilidad y adaptación del código, la función leer_sensor() centraliza esta operación y se reutiliza para ambos sensores.

Finalmente, el sistema muestra en consola únicamente el porcentaje de llenado de cada sensor, Además, el porcentaje se guarda en archivos de texto individuales para cada sensor, lo que facilita su posterior consulta o integración con otros sistemas. Las líneas relacionadas con la impresión y almacenamiento de la distancia original han sido comentadas intencionalmente, siguiendo un requerimiento específico, sin eliminar la funcionalidad subyacente para posibles usos futuros.

## Metodologia

Se realiza la conexion entre la raspberry pi y los sensores ultrasonido. 

![conexion_raspberry_ultrasonidos](/conexion_raspberry_ultrasonidos.jpeg)

Luego se realiza la lectura por medio de python.

![lectura_python.png](/lectura_python.png)

y por ultimo observamos los valores en node-RED.

![lectura_node_red](/lectura_node_red.png)