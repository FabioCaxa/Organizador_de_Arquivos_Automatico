import os
import shutil

atual = os.getcwd()

for pasta in os.listdir(atual):
    destino = os.path.join(atual, pasta)

    if os.path.isdir(destino):
        for arquivo in os.listdir(destino):
            aninhado = os.path.join(destino, arquivo)
            shutil.move(aninhado, atual)
        os.rmdir(destino)