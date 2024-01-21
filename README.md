# Organizador de Arquivos por Extensão

## Como funciona:

### Obtenção do diretório atual:
O script utiliza a biblioteca os para obter o diretório de trabalho atual, depois usa a função os.listdir para obter a lista de todos os arquivos no diretório atual.

### Iteração sobre os arquivos:
Depois itera sobre cada arquivo para obter o nome e a extensão usando a função os.path.splitext.

### Verificação da extensão do arquivo:
Se a extensão do arquivo for ".py", o arquivo é ignorado. Caso contrário, continua para a próxima etapa. Isso foi pensado para que o proprio organizador não se perca em meio aos arquivos.

### Organização em pastas:
O script cria uma nova pasta com base na extensão do arquivo em letras maiúsculas (exceto o ponto inicial) e move o arquivo para essa pasta.

### Estrutura de Pastas Resultante:
O diretório de trabalho atual terá subpastas correspondentes às extensões dos arquivos, e os arquivos serão movidos para suas respectivas pastas.

<hr>

# Descompactador de Pastas:

## Como funciona:

### Obtenção do diretório atual:
O script usa a biblioteca os para obter o diretório de trabalho atual.

### Iteração sobre as pastas no diretório:
Itera sobre cada pasta no diretório atual.

### Movimentação de arquivos para o diretório principal:
Para cada pasta, move os arquivos aninhados de volta para o diretório principal. Feito isso, o programa deleta a pasta agora vazia.
<hr>
