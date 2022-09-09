def solution(record):
    answer = []
    log = []
    idList = {}
    
    for i in record: 
                   
        if i.split()[0] == 'Enter':
            idList[i.split()[1]] = i.split()[2]
            log.append([i.split()[1],1])
                       
        if i.split()[0] == 'Leave':
            log.append([i.split()[1],0])
        
        if i.split()[0] == 'Change':
            idList[i.split()[1]] = i.split()[2]
            
    for i in log:
            if i[1] == 1:
                answer.append(f"{idList[i[0]]}님이 들어왔습니다.")
            else:
                answer.append(f"{idList[i[0]]}님이 나갔습니다.")
    
    return answer