a = int(input())
k=1
M = [[0 for j in range(a)] for i in range(a)]
ai=0
aj=a
while k<=a*a:
  if k==a*a:
    M[a//2][a//2]=k
    break
  for i in range(ai,aj):
    for j in range(ai,aj):
      if i==ai and j!=aj-1:
        M[i][j]=k
        k+=1
      if i!=aj-1 and j==aj-1:
        M[i][j]=k
        k+=1
  for i in range(aj-1,ai-1,-1):
    for j in range(aj-1,ai-1,-1):
      if i==aj-1 and j!=ai:
        M[i][j]=k
        k+=1
      if i!=ai and j==ai:
        M[i][j]=k
        k+=1
  ai+=1
  aj-=1
for i in(M):
  print(*i)
