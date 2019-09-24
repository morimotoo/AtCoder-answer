# ABC141-C.py
# https://atcoder.jp/contests/abc141/tasks/abc141_c

X = list(map(int, input().split()))
N = [X[1]-X[2]]*X[0]
Q = []
for i in range(X[2]):
  Q.append(int(input()))
for i in range(X[2]):
  N[Q[i]-1]+=1
for result in N:
  if(result >= 1):
    print('Yes')
  else:
    print('No')