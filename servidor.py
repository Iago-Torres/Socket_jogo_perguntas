#servidor


from socket import * #Importando a Biblioteca Socket


host = gethostname() # Pegando nome do computador
port = 55551 # Porta utilizada no Socket

print(f'Host: {host} , Port {port}') # Mostrando onde está conectado

serv = socket(AF_INET, SOCK_STREAM)
serv.bind((host, port)) # Atribuindo a Função de Escutar
serv.listen(5) #Quantidade de clientes que o servidor pode escutar 



while True:
    con, adr = serv.accept() # Aceitando a Conexão
    print(f'Alguém se conectou na:', {port},",", {host}) # Uma mesagem de boas vindas e 
                                                         # demonstrando que a conexão foi aceita
    name = con.recv(1024) # Identificando Caracteres

    while True:
            msg = con.recv(1024) # Identificando Caracteres
            print(name.decode(),':', msg.decode()) # Print da mensagem do cliente 
