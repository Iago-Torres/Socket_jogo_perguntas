#cliente

from socket import * #Importando a Biblioteca Socket

host =gethostname() # Pegando nome do computador
port = 55551 # Porta utilizada no Socket
cli = socket(AF_INET, SOCK_STREAM) 
cli.connect((host, port)) # Mostrando ao clinte onde se conectar


name = input('Say your name:') # Personalização de nome
cli.send(name.encode()) # Transmissão de mensagens através do socket

#___________________________________________Início do Jogo___________________________________________# 
q1 = input( "Você gostaria de jogar um jogo? S/N \n---> R: ")
q1= q1.lower()


if q1== "s":
          print("Vambora então. O tema é Conhecimentos Gerais")
#___________________________________________Pergunta 1___________________________________________#          
         
          a=input("Qual o maior país da Europa? \n---> R: ")
          a=a.lower()
          cli.send(a.encode())
          if a=="rússia":
                    print("A Resposta "+a+" está CORRETA!")
          else:
                    print("Errou! A resposta é Rússia")

#___________________________________________Pergunta 2___________________________________________#
         
          b=input("Qual o ano que acabou a 2° Guerra Mundial?\n---> R: ")
          b=b.lower()         
          cli.send(b.encode())
          if b=="1945":
                    print("A Resposta "+b+" está CORRETA!")
          else:
                    print("Nope, não é "+b+" A resposta é 1945")

#___________________________________________Pergunta 3___________________________________________#        
          
          c=input("Qual o maior planeta do nosso Sistema Solar?\n---> R: ")
          c=c.lower()
          cli.send(c.encode())
          if c=="júpiter":
                    print("A Resposta "+c+" está CORRETA!")
          else:
                    print("Não, acho que não.. "+c+" está errado. A resposta é Júpiter")

#___________________________________________Pergunta 4___________________________________________#
          
          d=input("Qual foi o maior Império da História?\n---> R: ")
          d=d.lower()
          cli.send(d.encode())
          if d=="mongol":
                    print("A Resposta "+d+" está CORRETA!")                    
          else:
                    print("Essa foi uma pegadinha cruel, a resposta  certa é o Império Mongol")

#___________________________________________Pergunta 5___________________________________________#
         
          e=input("Qual o tipo de reação nuclear que se utiliza para ativar a bomba atômica?\n---> R: ")
          e=e.lower()
          cli.send(e.encode())
          if e=="fissão":
                    print("Você acertou a mais difícil, meus parabéns!!")
                    print("Muito obrigado por jogar :D. Alternando para o outro modo.")
          else:
                    print("Não, a resposta é Fissão Nuclear")
                    print("Muito obrigado por jogar :D. Alternando para o outro modo.")

#_________________________________________Alternando o modo_________________________________________#
                   
          while True: # Modo para o cliente digitar e aparecer no servidor
                        msg = input("Digite ---> ")
                        cli.send(msg.encode())  # Transmissão de mensagens através do socket
                    
                           

#___________________________________________Final do Jogo___________________________________________#
            
else:
    print("Poxa, criei com tanto carinho :(. Então mudando para o outro modo")
    quit
    while True: 
            msg = input("Digite ---> ")  
            cli.send(msg.encode()) # Transmissão de mensagens através do socket