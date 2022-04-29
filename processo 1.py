import socket

#processo 1 se conectando ao processo 2
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.connect(("localhost", 50002))
  print(s)
   
  # recebendo os parametros
  cod_inicial = input("\nDigite o código inicial: ")
  n = input("Digite o valor de n: ")
  parametros = str(cod_inicial) + ',' + str(n)
  message= "{0}".format(parametros)
  sen = message.encode() 

  # enviando a requisicao para o processo 2
  s.sendall(sen)

  # recebendo e imprimindo a chave gerada e os numeros primos encontrados
  dados = s.recv(1024)
  print('\nRespostas dos processos:\n')
  print(dados.decode())