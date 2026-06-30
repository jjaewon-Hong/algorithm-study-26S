def solution(number, limit, power):
    dp = [0] * (number + 1) 
    
    for i in range(1, number + 1) :
        for j in range(i, number + 1, i):
            dp[j] += 1
            
    score = 0
            
    for count in dp[1:] :
        if count > limit :
            score += power
        else :
            score += count
    
    return score