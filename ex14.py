
#DESTINAÇÃO IR VIA ECA #2
quantidade = int(input())
somaF = 0
somaJ = 0

for i in range(quantidade):
  tipo = str(input())
  valor = float(input())
  if (tipo=='F'):
    resultado = valor*0.06
    somaF += resultado
  elif(tipo=='J'):
    resultado = (valor*1)/100
    somaJ += resultado

print('{:.2f}'.format(somaF))
print('{:.2f}'.format(somaJ))


