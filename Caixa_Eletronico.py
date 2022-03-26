#Desenvolva um programa que simule a entrega de notas quando um cliente efetuar um saque em um caixa eletrônico. Os requisitos básicos são os seguintes:

#Entregar o menor número de notas;
#É possível sacar o valor solicitado com as notas disponíveis;
#Saldo do cliente infinito;
#Quantidade de notas infinito (pode-se colocar um valor finito de cédulas para aumentar a dificuldade do problema);
#Notas disponíveis de R$ 100,00; R$ 50,00; R$ 20,00 e R$ 10,00

valor = int(input("Informe o valor para efetuar o saque: R$"))
total= valor
cedula = 100
totalCedula = 0

while True:
  if total >= cedula:
    total -= cedula
    totalCedula += 1
  else:
    print(f"Total de {totalCedula} cedulas de R${cedula}")
    if cedula == 100:
      cedula = 50
    elif cedula == 50:
      cedula = 20
    elif cedula == 20:
      cedula = 10
    elif cedula == 10:
      cedula = 1
    totalCedula = 0
    if total == 0:
      break