open("/path/to/mars.jpg")

output:

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
FileNotFoundError: [Errno 2] No such file or directory: '/path/to/mars.jpg'

#Traceback mostra a sequência de eventos que levou ao erro, a linha "File <stdin..." indica onde o erro começou. #"FileNotFoundError" indica que o arquivo não foi encontrado

python3 open.py

Traceback (most recent call last):
  File "/tmp/open.py", line 5, in <module>
    main()
  File "/tmp/open.py", line 2, in main
    open("/path/to/mars.jpg")
FileNotFoundError: [Errno 2] No such file or directory: '/path/to/mars.jpg'

#Acima executamos um código para o python abrir o arquivo em uma função 'main()" e então chama essa função a #partir de um bloco "if", isso cria uma cadeia de chamadas de função que o Python segue ao tentar executar o #código, o que resulta em um rastreamento mais detalhado

