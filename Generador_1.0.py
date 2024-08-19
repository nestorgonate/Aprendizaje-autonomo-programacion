import random #Libreria para permitir elegir aleatoriamente
import string #Libreria para tener acceso a simbolos, letras y numeros
import flet as ui
import tkinter as tk
from tkinter import filedialog
def generador(e):
    contenido_contrasena = string.ascii_letters + string.punctuation + string.digits #Usando la libreria string accede a letras, simbolos y numeros para juntarlos
    contrasena = random.choices(contenido_contrasena, k=12) #Usando la libreria random elige de la variable contenido_contrasena contenido aleatorio, la k determina longitud
    contrasena = "".join(contrasena) #.join() convierte contrasena de lista a string
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Archivos de texto", "*.txt")])
    with open(file_path, "w") as archivo: #El with se usa para que al finalizar la accion, el proceso finalice para ahorrar recursos
        archivo.write(contrasena)
#Creacion UI
def main(page: ui.Page):
    page.title = "Generador de contraseñas"
    imagen = ui.Image(
        src="https://images.credly.com/images/5371ddc2-611e-4071-8480-8d8e2b2e3cdb/blob.png",
        width=250,
        height=250,
        fit = ui.ImageFit.CONTAIN
    )
    page.window_width = 500        # window's width is 200 px
    page.window_height = 700     # window's height is 200 px
    page.window_resizable = False  # window is not resizable
#Agregar a la UI
    page.add(
        ui.Column(
            [
                imagen
            ],
            alignment=ui.MainAxisAlignment.START,
        )
    )
    page.add(
        ui.Row(
            [
                ui.ElevatedButton("Clic para generar", width=250, height=250, on_click=generador),
            ],
            alignment = ui.MainAxisAlignment.CENTER,
        )
    )
ui.app(target=main)
