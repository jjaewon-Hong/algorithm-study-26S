def solution(n, m, section):
    count = 0
    answer = 0
    for sec in section :
        if count > sec :
            continue
        count = sec + m
        answer += 1
            
    return answer