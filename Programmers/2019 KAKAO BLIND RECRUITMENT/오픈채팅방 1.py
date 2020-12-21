from collections import defaultdict

def solution(record):
    answer = []
    users = defaultdict(str)
    newrecord = []
    for line in record:
        command = line.split()
        if command[0] == "Enter":
            users[command[1]] = command[2]
            newrecord.append('Enter ' + command[1])
        elif command[0] == "Leave":
            newrecord.append('Leave ' + command[1])
        elif command[0] == "Change":
            users[command[1]] = command[2]
    for line in newrecord:
        command = line.split()
        if command[0] == "Enter":
            answer.append('{}님이 들어왔습니다.'.format(users[command[1]]))
        elif command[0] == "Leave":
            answer.append('{}님이 나갔습니다.'.format(users[command[1]]))
    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]),["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."])