# 백준 22864: 피로도
# https://www.acmicpc.net/problem/22864

# a = 5 ; b = 3 ; c = 2 ; m = 10
a, b, c, m = map(int, input().split())

x = 0 # 시간
A = 0 # 피로도
B = 0 # 처리한 일

if a > m:
    print(0)
else:
    while x < 24:
        x += 1
        if A + a <= m: # 번아웃 오기 전까지 
            A += a # 피로도 추가
            B += b # 일 처리 
        else: # 피로도가 m 이상 쌓이면 쉬기
            if A - c >= 0: # 쉬었을때 피로도 양수이면
                A -= c # 쉬기
            else: # 음수면
                A = 0 # 피로도 0
    print(B)


 