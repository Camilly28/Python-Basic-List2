# BALANÇO DE TRABALHOS
n = int(input())
for i in range(n):
  soma = 0
  nome=str(input())
  n2 = int(input())
  for k in range(n2):
    nota=float(input())
    soma = soma+nota
  div = soma/n2
  print(nome,'{:.2f}'.format(div))