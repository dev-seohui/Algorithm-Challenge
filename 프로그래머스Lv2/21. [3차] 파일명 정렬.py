def head(name):
    for i in range(len(name)):
        if name[i].isdigit():
            return name[:i]

def number(name):
    new_name = name.replace(head(name), "")
    num = ""
    for i in range(len(new_name)):
        if new_name[i].isdigit():
            num += new_name[i]
        else:
            break
    return num
 
def tail(name):
    new_name = name.replace(head(name), "").replace(number(name), "")
    return new_name

def solution(files):
    indexed_list = []
    
    for idx, value in enumerate(files):
        indexed_list.append((idx, head(value).lower(), int(number(value)), tail(value).lower().strip()))
    
    indexed_list = sorted(indexed_list, key=lambda x: (x[1], x[2], x[0]))
    answer = [files[idx] for idx, _, _, _ in indexed_list]
    return answer
