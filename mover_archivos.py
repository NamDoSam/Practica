#importar os para el manejo de archivos
import os
#importar shutil para mover archivos de un disco a cualquier disco
import shutil

downloadfolder = 'C:/Users/mpala/Downloads/'
musicfolder = 'F:/Musica/'
softfolder = "F:/software/"
pdffolder = "F:/pdf para ver/"
officefolder = "F:/Office para ver/"
videosfolder = "C:/Users/mpala/Videos/"
compressfolder = "F:/RAR para ver/"
ebooksfolder = 'F:/Ebooks/'

if __name__ == '__main__':
    for filename in os.listdir(downloadfolder):
        name, extension = os.path.splitext(downloadfolder + filename)

        if extension in ['.mp3']:
            shutil.move(downloadfolder + filename, musicfolder + filename)

        if extension in ['.exe', '.msi']:
            shutil.move(downloadfolder + filename, softfolder + filename)

        if extension in ['.pdf']:
            shutil.move(downloadfolder + filename, pdffolder + filename)

        if extension in ['.xls', '.xlsx', '.xlsm','.doc', '.docx', '.ppt', '.pptx']:
            shutil.move(downloadfolder + filename, officefolder + filename)

        if extension in ['.mp4', '.srt', '.vtt']:
            shutil.move(downloadfolder + filename, videosfolder + filename)

        if extension in ['.rar', '.zip']:
            shutil.move(downloadfolder + filename, compressfolder + filename)

        if extension in ['.epub']:
            shutil.move(downloadfolder + filename, ebooksfolder + filename)