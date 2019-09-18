# https://atcoder.jp/contests/abc141/tasks/abc141_a
today = input()
tenki = ['Sunny','Cloudy','Rainy','Sunny']
for i in range(3):
  if(tenki[i] == today):
    tomorrow = tenki[i+1]
print(tomorrow)