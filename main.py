def descobrir_palavra_secreta(palavra_secreta):
   # Iniciar uma lista para armazenar as letra adivinhadas corretamente
  palavra_descoberta = ['_' for _ in palavra_secreta]

  # DEfinir o numero maximo de tentativas
  tentativas_restantes = 0

  # Loop ate que a palavra seja descoberta

  # Solicitar uma letra ao usuario
  letra = input("Digite uma letra:").lower()

  #verificar se a letra esta na palavra secreta
  if letra in palavra_secreta:
     print(f"Boa! A letra'{letra}' esta na palavra")
     # Substituir os underlines pelas letras correspondentes
     for i in range(len(palavra_secreta)):
         if palavra_secreta[i]== letra:

          palavra_descoberta[i] = letra
         else:
          print("A letra não esta na palavra")    

  # Verificar se o usuario descobriu a palavra
  if '_' not in palavra_descoberta:
        print(f"Você descobriu a palavra:{''.join(palavra_descoberta)}")

  # Palavra secreta a ser descoberta
  palavra_secreta = "neymar"
  descobrir_palavra_secreta(palavra_secreta)
