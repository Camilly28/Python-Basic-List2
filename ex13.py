
# DESTINAÇÃO IR VIA ECA #1
pessoa = str(input()) #J ou F
valor = float(input())
resultado=0
if (pessoa=='F'):
  resultado = (valor*6)/100
  print('{:.2f}'.format(resultado))
elif(pessoa=='J'):
  resultado = (valor*1)/100
  print('{:.2f}'.format(resultado))

