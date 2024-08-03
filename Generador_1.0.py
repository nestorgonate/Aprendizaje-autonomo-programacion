import random #Libreria para permitir elegir aleatoriamente
import string #Libreria para tener acceso a simbolos, letras y numeros
pregunta = input("Quieres generar una contraseña?(Si/No): ").lower()
def generador():
    contenido_contrasena = string.ascii_letters + string.punctuation + string.digits #Usando la libreria string accede a letras, simbolos y numeros para juntarlos
    contrasena = random.choices(contenido_contrasena, k=12) #Usando la libreria random elige de la variable contenido_contrasena contenido aleatorio, la k determina longitud
    contrasena = "".join(contrasena) #.join() convierte contrasena de lista a string
    print(contrasena)
if pregunta == "si":
    generador()
elif pregunta == "no":
    print("Hasta luego")
else:
    print("Ingresa una respuesta valida")
