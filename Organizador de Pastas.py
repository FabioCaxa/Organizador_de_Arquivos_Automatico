import os
import shutil

atual = os.getcwd()
arquivos = os.listdir(atual)

for arquivo in arquivos:
    nome, extensao = os.path.splitext(arquivo)

    if extensao == ".py":
        pass
    else:
        nova_pasta = os.path.join(atual, extensao.upper()[1:])
        if not os.path.exists(nova_pasta):
            os.makedirs(nova_pasta)
        shutil.move(os.path.join(atual, arquivo), os.path.join(nova_pasta, arquivo))