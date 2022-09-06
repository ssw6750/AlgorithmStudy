def solution(new_id):
    answer = ''
    temp = ''
    
    new_id = new_id.lower()
    
    for i in range(len(new_id)):
        char = new_id[i]
        if char.islower() or char.isdigit() or char == '-' or char == '_' or char == '.':
            temp += char
            
    
    while(True):
        if '..' in temp:
            temp = temp.replace('..', '.', len(temp))
        else:
            break
            
    temp = temp.strip('.')
    
    if temp == '':
        temp = 'a'
        
    
    if len(temp)>=16:
        temp = temp[0:15]
        
    temp = temp.strip('.')

    
    while(True):
        if len(temp)<=2:
            temp += temp[-1]
        else:
            break
                   
    answer = temp
    
    return answer