# 백준 14916 거스름돈
# n = int(input())
n = 14
if n < 5: 
    cnt = 0
else:
    cnt = n // 5 
    n -= cnt*5 # 일단 5로 가능한 한 많이 거슬러준다

while n > 0:
    if cnt < 0: 
        cnt = -1
        break
    if n%2 == 0: # 나머지가 2로 전부 나누어떨어지면
        cnt += n//2 # 2로 거슬러주기
        break
    else: # 2로 전부 나누어떨어지지 않으면
        n += 5 # 5만큼 다시 더해고
        cnt -= 1

print(cnt)