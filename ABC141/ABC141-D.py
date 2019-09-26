# ABC141-D.py
# D - Powerful Discount Tickets
# https://atcoder.jp/contests/abc141/tasks/abc141_d
# 大きい順に半分(小数点切り捨て))にしていく
# 優先度付きキューを用いないと時間制限内に終わらない
import heapq
X = list(map(int, input().split()))
# A = list(map(int, input().split()))
A = list(map(lambda x: int(x)*(-1), input().split())) # 最大値を取るために各要素を-1倍
heapq.heapify(A)

for i in range(X[1]):
  x = heapq.heappop(A) * (-1) # 最大値の取り出し
  heapq.heappush(A, int(x/2) * (-1))

ans = 0
for i in range(X[0]):
  ans -= A[i]

print(ans)