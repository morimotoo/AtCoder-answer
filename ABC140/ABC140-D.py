# ABC140-D.py
# https://atcoder.jp/contests/abc140/tasks/abc140_d
N, K = map(int,input().split())
S = input()
count_RL = 0
for i in range(N-1):
    if S[i] == 'R' and S[i+1] == 'L':
        count_RL += 1
count_edge = 0
if S[0] == 'L':
    count_edge += 1
if S[N-1] == 'R':
    count_edge += 1
count_K = 0
for i in range(K):
    if count_RL == 0:
        break
    count_RL -= 1
    count_K += 1
if (K - count_K) > 0:
    count = K - count_K
    if count_edge == 2:
        count_edge -= 1
if count_edge == 0 and count_RL == 0:
    count_edge = 1
    
not_happy = N - 2*count_RL - count_edge
print(not_happy)

