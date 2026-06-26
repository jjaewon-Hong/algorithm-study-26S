from itertools import combinations as cb

def solution(number):
    answer = 0
    
    for c in cb(number,3) :
        if sum(c) == 0 :
            answer += 1
            
    return answer