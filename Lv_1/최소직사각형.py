def solution(sizes):
    maxw = 0
    maxh = 0
    
    for size in sizes :
        w = max(size)
        h = min(size)
        
        maxw = max(maxw, w)
        maxh = max(maxh, h)
        
    return maxw * maxh