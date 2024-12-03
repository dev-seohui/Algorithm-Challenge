def solution(bridge_length, weight, truck_weights):
    
    on_weight, on_length, time = 0, 0, 0
    on_bridge = [0]*bridge_length
    
    while truck_weights or on_weight > 0:
        time += 1
        on_weight -= on_bridge.pop(0)
        on_bridge.append(0)
        
        if truck_weights and (on_weight + truck_weights[0] <= weight):
            current = truck_weights.pop(0)
            on_weight += current
            on_bridge[-1] = current
    return time
