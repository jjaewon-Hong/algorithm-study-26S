# 앞에서 부터 오름차순으로 채우기 X
# => 앞, 뒤 같이 태우는 방식

def solution(people, limit):
    people.sort()
    
    left = 0
    right = len(people) - 1
    answer = 0
    
    while left <= right :
        if people[left] + people[right] <= limit :
            left += 1
        
        right -= 1
        answer += 1

    return answer