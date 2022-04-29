import socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

  s.bind(('', 8080))
  print(s)
  s.listen()

  # conexão com o processo 2
  while True:
        conexao, addr = s.accept()
    
        with conexao:
            print(f"\n\nProcesso 2 conectado: {addr}")
            dados = conexao.recv(1024)
            
            # normalizando os valores recebidos
            request = dados.decode('utf-8')
            request = request.split(",")
            num1 = int(request[0])
            num2 = int(request[1])
            
            # gerando a chave
            resultado = num1*num2
            
            message= "{0}".format(resultado)
            sen = message.encode()  
            
            print ('\nChave gerada: ',resultado)
            
            conexao.sendall(sen)