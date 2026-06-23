def solution(n, lost, reserve):
    # 차집합 처리
    actual_lost = list(set(lost) - set(reserve))
    actual_reserve = list(set(reserve) - set(lost))
    
    actual_lost.sort()
    actual_reserve.sort()
    
    for r in actual_reserve :
        if r-1 in actual_lost :
            actual_lost.remove(r-1)
        elif r+1 in actual_lost :
            actual_lost.remove(r+1)

    return n - len(actual_lost)