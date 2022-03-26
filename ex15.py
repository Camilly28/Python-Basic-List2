

#14- Tabuada flexivel
n1 = int(input())
n2 = int(input())
n3 = int(input())
print('Tabuada do',n1,'de',n2,'até',n3)
for i in range(n2,n3): 
  print(n1,'x',i,'=',i*n1)
#---------------------
n1 = int(input())
n2 = int(input())
n3 = int(input())
print('Tabuada do',n1,'de',n2,'até',n3)
for i in range(n2,n3+1): 
  z = n1*i
  print(n1,'x', i,'=', z)

