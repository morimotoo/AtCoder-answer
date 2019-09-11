N = int(input())
grid = []
A = list(map(int, input().strip().split()))
Ai = [n-1 for n in A]
B = list(map(int, input().strip().split()))
C = list(map(int, input().strip().split()))
ans = 0
for i in range(N):
  ans += B[Ai[i]]
  if((i > 0) and (Ai[i] == Ai[i-1]+1)):
  	ans += C[Ai[i-1]]
print(ans)
