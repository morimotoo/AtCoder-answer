# ABC141-B.py
# https://atcoder.jp/contests/abc141/tasks/abc141_b
s = input()
result = 'Yes'
for i in range(len(s)):
  if (i%2==0):
    if (s[i] == 'L'):
    	result = 'No'
  else:
    if (s[i] == 'R'):
    	result = 'No'
print(result)
