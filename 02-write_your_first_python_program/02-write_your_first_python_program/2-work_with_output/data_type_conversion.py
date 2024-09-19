from datetime import date
date.today()
print(date.today())
print("Today's date is: " + str(date.today()))

#Explicando o código
from datetime import date: Esta linha importa a classe date do módulo datetime. A classe date permite representar datas no Python.

date.today(): Esta linha cria uma instância da classe date que representa a data atual. O método today() é chamado sem nenhum argumento e retorna a data atual do sistema.

print(date.today()): Aqui, a data atual é impressa no formato padrão, que é algo como "ano-mês-dia" (por exemplo, "2023-09-18").

print("Today's date is: " + str(date.today())): Nesta linha, a data atual é convertida em uma string usando a função str() para que possa ser concatenada com a mensagem "Today's date is: ". Em seguida, a mensagem completa é impressa na tela. O resultado será algo como "Today's date is: 2023-09-18".