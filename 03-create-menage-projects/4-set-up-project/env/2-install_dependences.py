# criar um diretório e acessar por linha de comando

md src
cd src

# com os comandos abaixo iremos criar os arquivos vazios

type nul > app.py
type nul > requirements.txt

# adicionando o conteúdo abaixo em /env/scripts/src/app.py

from datetime import *
from dateutil.relativedelta import *
now = datetime.now()
print(now)

now = now + relativedelta(months=1, weeks=1, hour=10)

print(now)

# adicionando o conteúdo abaixo em requeriments.txt

python-dateutil==2.8.2
six==1.16.0

$ instalando as bibliotecas

pip install -r requirements.txt