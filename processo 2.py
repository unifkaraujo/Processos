import math
import socket
import sympy

# processo 2 calcula os numeros primos e os envia para o processo 3 calcular a chave 

# conexao com o processo 1
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    
    s.bind(('', 50002))
    print(s)
    s.listen()

    while True:
        conexao, addr = s.accept()
        with conexao:
            print(f"\n\nProcesso 1 conectado: {addr}")
            while True:
                dados = conexao.recv(1024)
                
                if not dados:
                    break
                
                # normalizando os valores passados
                dados = dados.decode('utf-8')
                dados = dados.split(",")
                
                cod_inicial = int(dados[0])
                n = int(dados[1])
                
                if (cod_inicial >= 1000000 and n >= 5000 and n <= 15000):
                    
                    # calculando os primos a esquerda do numero
                    i = cod_inicial
                    vet = []
                    qtdvetor = 0
                
                    while (qtdvetor < n):
                        i = i-1
                              
                        if sympy.isprime(i):
                            vet.append(i)
                                                    
                        qtdvetor = len(vet)
                    
                    primoleft = qtdvetor - 1
                                
                    # calculando os primos a direita do numero
                    i = cod_inicial
                    vetdir = []
                    qtdvetordir = 0
                
                    while (qtdvetordir < n):
                        i = i+1

                        if sympy.isprime(i):
                            vetdir.append(i)
                        
                        qtdvetordir = len(vetdir)
                     
                    primodir = qtdvetordir - 1
                               
                    # encontrado os numeros primos, normalizo os dados e envio a requisicao para o processo 3 calcular a chave
                    numencontrados = str(vet[primoleft]) + ' <------ ' + str(cod_inicial) + ' ------> ' + str(vetdir[primodir])
                    valores = str(vet[primoleft]) + ',' + str(vetdir[primodir])
                    message= "{0}".format(valores)
                    sen = message.encode()  
                 
                    # conexão com o processo 3
                    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as t:
                        t.connect(("localhost", 8080))
                        t.sendall(sen)
                        chavegerada = t.recv(1024)
                    
                    print ('\nNúmeros encontrados no processo 2: ')
                    print (numencontrados)
                    
                    print ('\nChave gerada pelo processo 3: ')
                    print (chavegerada.decode())
                    
                    resp_proc1 = 'Números encontrados no processo 2:' + '\n' + numencontrados + '\n\n' + 'Chave gerada pelo processo 3: ' + '\n' + chavegerada.decode()
                    message= "{0}".format(resp_proc1)
                    sen = message.encode()  
                    
                    conexao.sendall(sen)
                else:
                    error = 'O código inicial precisa ser >= 1000000 e (5.000 <= n <= 15000)'
                    message= "{0}".format(error)
                    sen = message.encode()  
                    print ('Processamento não realizado')
                    print (error)
                    conexao.sendall(sen)