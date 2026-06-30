def solution(k, score):
    answer = []
    temp = []
    for s in score :
        temp.append(s)
        temp.sort(reverse=True)
        if len(temp) > k :
            temp = temp[:k]
            # 앞에서부터 k만큼만 가져오기

        answer.append(temp[-1])
    
    return answer
