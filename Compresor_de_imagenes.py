#importar pillow para el manejo de las imagenes
from PIL import Image
#Importar os para el manejo de los archivos
import os
#definir el directorio
downloadfolder = "C:/Users/mpala/Downloads/para_comprimir/"
picturefolder = "C:/Users/mpala/Pictures/para revisar/"
if __name__ == "__main__":
    for filename in os.listdir(downloadfolder):
        name, extension = os.path.splitext(downloadfolder + filename)

        if extension in [".jpg", ".jpeg", ".png", ".gif"]:
            picture = Image.open(downloadfolder + filename)
            picture.save(picturefolder + filename, optimize = True, quality = 60)
            os.remove(downloadfolder + filename)
