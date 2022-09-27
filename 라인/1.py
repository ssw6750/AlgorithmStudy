from collections import defaultdict

queries = [[2, 10], [7, 1], [2, 5], [2, 9], [7, 32]]
queries1 = [[1, 1], [1, 2], [1, 4], [1, 8]]

def solution(queries):
    d = defaultdict(list)
    answer = 0

    for i in queries:
        v, c = i[0], i[1] # 배열 번호, 추가할 원소의 수를 받는다 
        if d[v] == []: # 해당 배열 번호의 배열리 처음 만들어진 경우
            i = 0
            while 2**i<=c:
                i+=1
            d[v] = [i, c] # 2n승의 n의 값을 딕셔너리에 넣는다.
        else:
            tmp = d[v][1] + c # 이미 해당 배열 번호의 배열이 나왔던 경우
            d_i = d[v][0]
            if tmp > 2**d_i: # 배열의 크기(2**n)보다 큰 경우
                answer+= d[v][1] # 이미 존재하는 원소의 수를 answer에 더함 (복사하는 배열의 수)
                while 2**d_i<=tmp: # 배열의 크기를 다시 만든다
                    d_i+=1
                d[v] = [d_i, tmp]
            else: d[v] = [d_i, tmp] # 배열의 크기(2**n)보다 작은 경우 경우

    print(answer)


solution(queries)
solution(queries1)