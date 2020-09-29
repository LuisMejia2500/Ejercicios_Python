def Comparador(A,B):
  if (A==B):
    val="SI"
    return (val)
  else:
    val="NO"
    return (val)


A=(input())
B=(input())
B=B[::-1]

print(Comparador(A,B))
