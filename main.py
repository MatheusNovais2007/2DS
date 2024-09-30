def descobrir_palavra_secreta(palavra_secreta):
   
  palavra_descoberta = ['_' for _ in palavra_secreta]

  
  tentativas_restantes = 0

  # Loop ate que a palavra seja descoberta

 
  letra = input("Digite uma letra:").lower()

  
  if letra in palavra_secreta:
     print(f"Boa! A letra'{letra}' esta na palavra")
     
     for i in range(len(palavra_secreta)):
         if palavra_secreta[i]== letra:

          palavra_descoberta[i] = letra
         else:
          print("A letra não esta na palavra")    

  
  if '_' not in palavra_descoberta:
        print(f"Você descobriu a palavra:{''.join(palavra_descoberta)}")

  # Palavra secreta a ser descoberta
  palavra_secreta = "neymar"
  descobrir_palavra_secreta(palavra_secreta)
