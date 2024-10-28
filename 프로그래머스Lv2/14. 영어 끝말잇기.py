
def solution(n, words):
    answer = []
    used = set()
    previous_word = ""
    
    for i, value in enumerate(words):
        if words[i] in used:
            return [(i%n+1), (i//n+1)]
        if i>0 and value[0] != previous_word[-1]:
            return [(i%n+1), (i//n+1)]
        
        used.add(value)
        previous_word = value
    return [0, 0]
