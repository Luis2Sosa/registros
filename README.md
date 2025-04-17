# 📌 Proyecto: Data Detector Logger

Aplicación de consola en Python que detecta y registra datos sensibles utilizando expresiones regulares.

---

## 🚀 ¿Qué hace esta app?

Este sistema permite detectar automáticamente los siguientes datos dentro de un texto:

- 📨 Correos electrónicos
- 🪪 Cédulas dominicanas (formato `000-0000000-0`)
- 📅 Fechas (formato `dd/mm/aaaa`)
- 🔐 Contraseñas seguras (mínimo 8 caracteres, con mayúscula, minúscula, número y símbolo)

Cada tipo de dato detectado se guarda en un **archivo de texto independiente**, con su nombre y fecha/hora exacta. Todos los archivos se almacenan automáticamente dentro de la carpeta `registros`.

---

## 📁 Estructura de Archivos

registros/ ├── correos_16-04-2025_22-30-00.txt ├── cedulas_16-04-2025_22-30-01.txt ├── fechas_16-04-2025_22-30-02.txt ├── contraseñas_16-04-2025_22-30-03.txt


---

## 🧠 Tecnologías usadas

- Python 3
- Módulo `re` (Expresiones Regulares)
- Módulo `os`
- Módulo `datetime`

---

## 🎮 Cómo usarlo

1. Clona este repositorio o descarga el archivo `.py`.
2. Ejecuta el script en consola:
   ```bash
   python nombre_del_archivo.py

Elige una opción del menú interactivo.

El sistema detectará los datos y los guardará automáticamente en la carpeta registros.

🧪 Ejemplo de detección
Texto de entrada:

"Puedes escribirnos a info@empresa.com, ver tu ID 001-2345678-9 o verificar tu acceso con Sosa43!22 el día 15/08/2023."

Salida esperada:

Detecta el correo

Detecta la cédula

Detecta la fecha

Detecta la contraseña segura

Guarda cada dato en su archivo respectivo

✅ Características clave
Detección precisa usando expresiones regulares avanzadas.

Organización automática de archivos por tipo y fecha.

Menú interactivo de consola para facilitar el uso.

Formato de salida profesional, listo para revisión o auditoría de datos.

👨‍💻 Autor
Creado por Luis Sosa
Proyecto parte de su entrenamiento como desarrollador Python junior, enfocado en automatización, lógica y validación de datos reales.