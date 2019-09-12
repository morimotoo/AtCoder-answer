N = int(input())
B = list(map(int, input().strip().split()))
A=[1000000] * (N)

for i in range(N-1):
  if B[i] < A[i]:
    A[i] = B[i]
    A[i+1] = B[i]
  else:
    A[i+1] = B[i]
A_sum=0
for x in A:
  A_sum+=x
print(A_sum)