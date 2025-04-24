# Importamos los módulos
import os
import re
from datetime import datetime

carpeta1 = "registros"

# Mensaje en consola
print("--- REGISTRO DE ARCHIVOS ---\n")

# Mostramos el menu
def menu():
    print("Puedes registrar...\n")
    print("1. Correos electrónicos")
    print("2. Cedulas")
    print("3. Fechas")
    print("4. Contraseñas (seguras o inseguras)")
    print("5. Salir\n")
    
# Trabajamos con las funciones
def detectar_correos(texto):
    patron = r"[\w\.-]+@[\w\.-]+\.\w{2,}"
    correos = re.findall(patron, texto)
    
    fecha = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
    
    
    if not os.path.exists(carpeta1):
        os.mkdir(carpeta1)
        print(f"La carpeta '{carpeta1}' fue creada.")
    else:
        print("La carpeta ya existe.")
    
    nuevo_archivo = f"correos_{fecha}.txt"
    nueva_ruta = os.path.join(carpeta1, nuevo_archivo)
    
    with open(nueva_ruta, "a") as archivo:
        if correos:
            print("Correos encontrados:")
            for correo in correos:
                print(f"- {correo}")
                archivo.write(f"[{fecha}] Correos encontrados: {correo}\n")
        else:
            print("No se encontraron correos.")
            archivo.write(f"[{fecha}] No se encontraron correos.")    

texto1 = "Puedes comunicarte a luis27@hotmail.com o jose43@gmail.com."

def detectar_cedulas(texto):
    patron = r"\d{3}-\d{7}-\d{1}"
    cedulas = re.findall(patron, texto)
    
    fecha = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
    
    nuevo_archivo = f"cedulas_{fecha}.txt"
    nueva_ruta = os.path.join(carpeta1, nuevo_archivo)
    
    with open(nueva_ruta, "a") as archivo:
        if cedulas:
            print("Cedulas encontradas:")
            for cedula in cedulas:
                print(f"- {cedula}")
                archivo.write(f"[{fecha}] Cedulas encontradas: {cedula}\n")
        else:
            print("No se encontraron cedulas.")
            archivo.write(f"[{fecha}] No se encontraron cedulas.")

texto2 = "Se encontraron las siguientes cedulas en el banco. 402-2543985-5 y 001-8348657-8." 

def detectar_fechas(texto):
    patron = r"\b(?:0[1-9]|1[0-9]|2[0-9]|3[0-1])/(?:0[1-9]|1[0-2])/\d{4}"
    fechas = re.findall(patron, texto)
    
    fecha = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
    
    nuevo_archivo = f"fechas_{fecha}.txt"
    nueva_ruta = os.path.join(carpeta1, nuevo_archivo)
    
    with open(nueva_ruta, "a") as archivo:
        if fechas:
            print("Fechas encontradas:")
            for f in fechas:
                print(f"- {f}")
                archivo.write(f"[{f}] Fechas encontradas: {f}\n")
        else:
            print("No se encontraron fechas.")
            archivo.write(f"[{fecha}] No se encontraron fechas.")
            
texto3 = "El 19/08/1994 fue un año muy importante, aunque en 16/03/1886 también." 

def detectar_contraseña(texto):
    patron = r"(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%])(?=.*\d)[a-zA-Z!@#$%\d]{8,}"
    contraseñas = re.findall(patron, texto)
    
    fecha = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
    
    nuevo_archivo = f"contraseñas_{fecha}.txt"
    nueva_ruta = os.path.join(carpeta1, nuevo_archivo)
    
    with open(nueva_ruta, "a") as archivo:
        if contraseñas:
            print("Contraseñas encontradas:")
            for contaseña in contraseñas:
                print(f"- {contaseña}")
                archivo.write(f"[{fecha}] Contraseñas encontradas: {contaseña}\n")
        else:
            print("No se encontraron contraseñas.")
            archivo.write(f"[{fecha}] No se encontraron contraseñas.")

texto4 = "Aveces uso Luis2992@ para entrar y Sosa43!22 para salir." 

# Bucle para llamar las funciones 
while True:
    menu()
    opcion = int(input("Elija un numero de opción:\n"))
    
    if opcion == 1:
        detectar_correos(texto1)
    elif opcion == 2:
        detectar_cedulas(texto2)
    elif opcion == 3:
        detectar_fechas(texto3)
    elif opcion == 4:
        detectar_contraseña(texto4)
    elif opcion == 5:
        print("Gracias por usar el --- REGISTRO DE ARCHIVOS ---\n")
        break
    else:
        print("Opción no valida. Intente de nuevo")
        
# ✅ Progreso guardado por Luis Sosa – revisión 24 de abril
