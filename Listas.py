def Comprobacion(X,N):
  Suma=0
  for i in range (0,N):
    Suma=Suma+ X[i]

  if Suma==0:
    A="FACIL"
    return(A)
    
  else:
    A="DIFICIL"
    return(A)

N=int(input())
Y=tuple(map(int, input().split()))
X=list(Y)

print(Comprobacion(X,N))


