# record = ["Enter uid1234 Muzi", 
#         "Enter uid4567 Prodo",
#         "Leave uid1234",
#         "Enter uid1234 Prodo",
#         "Change uid4567 Ryan"]

# result = ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]
def solution(record):
    answer = []

    dict = {} # uid : nickname
    output = []
    for message in record:
        elc = message.split()[0]
        uid = message.split()[1]

        if elc == 'Enter':
            nickname = message.split()[2]
            dict[uid] = nickname
            output.append([uid, '님이 들어왔습니다.'])
        if elc == 'Change':
            nickname = message.split()[2]
            dict[uid] = nickname
        if elc == 'Leave':
            output.append([uid, '님이 나갔습니다.'])

    for m in output:
        m[0] = dict[m[0]]
        answer.append(m[0]+m[1])

    return answer
