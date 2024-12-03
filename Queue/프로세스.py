def solution(priorities, location):
    
    queue = [(index, value) for index, value in enumerate(priorities)]
    order = 0
    
    while queue:
        current = queue.pop(0)
        if any(current[1] < q[1] for q in queue):
            queue.append(current)
        else:
            order += 1
            if current[0] == location:
                return order
        
