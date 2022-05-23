# def solution(survey, choices):
#     answer = ''
#     return answer
# import numpy as np
survey = ["AN", "CF", "MJ", "RT", "NA"]
choices = [5, 3, 2, 7, 5]

index = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}
score = dict({1:3, 2:2, 3:1, 4:0, 5:1, 6:2, 7:3}) # 매우 비동의 ~ 매우 동의 => 0 ~ 3점 점수 매핑
n = len(choices) # 질문 개수

for i in range(n):
    if choices[i] <= 3: # 비동의 캐릭터
        char = survey[i][0]
        scr = score[choices[i]] 
        index[char] += scr # 비동의 캐릭터의 점수 더해주기 

    if choices[i] >= 5: # 동의 캐릭터
        char = survey[i][1]
        scr = score[choices[i]]
        index[char] += scr # 동의 캐릭터의 점수 더해주기 

    if choices[i] == 4: # 모르겠음
        pass # 아무 캐릭터도 점수 얻지 못함

print(index)

index2 = [['R','T'],['C','F'],['J','M'],['A','N']]
answer = ''
for i in range(4):
    if index[index2[i][0]] == index[index2[i][1]]:
        answer += min(index2[i])
    elif index[index2[i][0]] > index[index2[i][1]]:
        answer += index2[i][0]
    else: 
        answer += index2[i][1]

print('answer:', answer)