#1978-소수찾기

N=int(input())
N_list = list(map(int, input().split()))
count = 0

for i in N_list :
  check = 0
  if i == 1 :
    continue
  for j in range(2, i) :
    if i % j == 0 :
      check = 1
  
  if check == 0 :
    count += 1

print(count)