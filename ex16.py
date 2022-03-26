
#BALANÇA DE PROVA
meninas =int(input())
#print('Total de meninas: ',meninas)
notamax=0
notamin=0
notarecup=0
for i in range(0,meninas):
  nota =float(input()) 
  if (nota==10.0):
   notamax = notamax +1

  if (nota>=5.0):
   notamin = notamin +1

  if (nota<5.0):
   notarecup = notarecup +1

print('Total de meninas: ',meninas)
print('Meninas com nota máxima na prova: ',notamax)
print('Meninas com nota mínima na prova: ',notamin)
print('Meninas que devem fazer prova de recuperação: ',notarecup)


