import socket
import time
import random

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
  inicio = time.time()
  s.sendall(sen)
    
  # recebendo e imprimindo a chave gerada e os numeros primos encontrados
  dados = s.recv(1024)
  fim = time.time()
  tempo = (fim-inicio)

  print('\nRespostas dos processos:\n')
  print(dados.decode())
    
  print('\nTempo de execução dos processos: %f'%(tempo))

  # Aqui inicio a execução de chaves aleatórias
  print('\n\n----------------------------------------------------------')
  print('Objetivo 2: Geração do máximo de chaves em 5 segundos')
  print('\nChaves Geradas: ')
  inicio = time.time()
  cont = 0
    
  while (tempo < 5.0):
    cod_inicial = random.randint(10000001,20000000)
    n = random.randint(5000,15000)
    parametros = str(cod_inicial) + ',' + str(n)
    message= "{0}".format(parametros)
    sen = message.encode()
    s.send(sen)
    dados = s.recv(1024)
    dados = dados.decode('utf-8')
    dados = dados.split(" ")
    fim = time.time()    
    tempo = fim - inicio
    cont += 1
    
    print (dados[13])

  print ('\nTotal de chaves geradas em 5 segundos: ', cont)
  print('----------------------------------------------------------')