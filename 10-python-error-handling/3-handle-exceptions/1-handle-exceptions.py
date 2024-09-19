#O usuário pode se deparar com algum erro, é útil permitir que excessões sejam geradas para que os outros usuários #ou desenvolvedores possam lidar com os erros: 

try:
     open('config.txt')
except FileNotFoundError:
     print("Couldn't find the config.txt file!")

#Aqui o usuário vai receber uma mensagem de aviso, "Couldn't find the config.txt file!" caso ele não encontre o #arquivo config.txt.

def main():
    try:
        configuration = open('config.txt')
    except FileNotFoundError:
        print("Couldn't find the config.txt file!")
    except IsADirectoryError:
        print("Found config.txt but it is a directory, couldn't read it")
    except (BlockingIOError, TimeoutError):
        print("Filesystem under heavy load, can't complete reading configuration file")

#Aqui o usuário vai receber mais mensagens de aviso, caso enfrente outros erros, como erros de permissão