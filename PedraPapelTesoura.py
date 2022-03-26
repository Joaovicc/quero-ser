#O objetivo é fazer um juiz de Jokenpo que dada a jogada dos dois jogadores informa o resultado da partida.
#As regras são as seguintes:
#-Pedra empata com Pedra e ganha de Tesoura
#-Tesoura empata com Tesoura e ganha de Papel
#-Papel empata com Papel e ganha de Pedra


print(''' ESCOLHA SUAS OPÇÕES:
       PEDRA
       PAPEL
       TESOURA''')

a = input("1° Jogador escolha uma das tres opções acima: ")
b = input("2° Jogador escolha uma das tres opções acima: ")

if (a != "Pedra" and a != "Papel" and a != "Tesoura" and
    b != "Pedra" and a != "Papel" and a != "Tesoura"):
  print("FIM DE JOGO!!!")

else:
  if (a == b):
    print("EMPATE")
  elif(a == "Pedra" and b == "Tesoura"):
    print("Jogador 1° Ganhou!!!")
  elif(a == "Pedra" and b == "Papel"):
    print("Jogador 1° Ganhou!!!")
  elif(a == "Pedra" and b == "Tesoura"):
    print("Jogador 2° Ganhou!!!")
  elif(a == "Papel" and b == "Tesoura"):
    print("Jogador 2° Ganhou!!!")
  elif(a == "Papel" and b == "Pedra"):
    print("Jogador 1° Ganhou!!!")
  elif(a == "Tesoura" and b == "Pedra"):
    print("Jogador 2° Ganhou!!!")
  elif(a == "Tesoura" and b == "Papel"):
    print("Jogador 1° Ganhou!!!")
  

