def solution(s, skip, index):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    for i in skip:
        alphabet = alphabet.replace(i, "")
        
    for i in range(len(s)+1):
        result += alphabet[(i+index)%len(alphabet)]
    return result
