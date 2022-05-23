# def solution(queue1, queue2):
#     answer = -2
#     return answer

queue1 = [3, 2, 7, 2]	
queue2 = [4, 6, 5, 1]
# q = queue1 + queue2 
# from itertools import combinations
q = [3, 2, 7, 2, 4, 6, 5, 1]
n = len(queue1)
target = (sum(queue1) + sum(queue2))/2
answer = -1

for i in range(2*n):
    sum = 0
    for j in range(2*n-i):
        sum += q[i+j]
        if sum == target:
            print(i, j)
            if (answer > i + (i+j-n+1)) or (answer == -1):
                answer = i + (i+j-n+1)
        if sum > target: 
            break
print(answer)

# for m in range(2, len(q)+1):
#     comb = list(combinations(q, m))
#     for i in range(len(comb)):
#         res = sum(comb[i])
#         if res == target:
#             print(comb[i])
#             print('ok')

# queue1 = [1, 2, 1, 2]
# queue2 = [1, 10, 1, 2]
# queue1 = [1, 1]
# queue2 = [1, 5]

# n = len(queue1)
# cnt = 0
# for _ in range(2**n):
#     if sum(queue1) > sum(queue2): # q1에서 빼서 q2에 넣기
#         print('sum1 > sum2')
#         queue2.append(queue1.pop(0))
#         cnt += 1
#         print('queue1=',queue1)
#         print('queue2=',queue2)
#         if sum(queue1) == sum(queue2):
#             break
#     if sum(queue1) < sum(queue2): # q2에서 빼서 q1에 넣기
#         print('sum2 > sum1')
#         queue1.append(queue2.pop(0))
#         cnt += 1
#         print('queue1=',queue1)
#         print('queue2=',queue2)
#         if sum(queue1) == sum(queue2):
#             break
#     # if cnt > 2**n:
#     #     print(-1)
#     #     break
# if sum(queue1) == sum(queue2):
#     print(cnt)
# else:
#     print(-1)


