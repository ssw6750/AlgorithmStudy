class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}

class Trie(object):
    def __init__(self):
        self.head = Node(None)
  # 문자열 삽입
    def insert(self, string):
        curr_node = self.head
        # 삽입할 string 각각의 문자에 대해 자식 Node를 만들며 내려간다.
        for char in string:
            # 자식 Node들 중 같은 문자가 없으면 Node 새로 생성
            if char not in curr_node.children:
                curr_node.children[char] = Node(char)
            # 같은 문자가 있으면 노드를 따로 생성하지 않고, 해당 노드로 이동
            curr_node = curr_node.children[char]
        #문자열이 끝난 지점의 노드의 data값에 해당 문자열을 입력
        curr_node.data = string
    # 문자열이 존재하는지 search

    def search2(self, string):
        #가장 아래에 있는 노드에서 부터 탐색 시작
        curr_node = self.head
        for char in string:
            if char in curr_node.children:
                curr_node = curr_node.children[char]
            else:
                return False
        return True
        


for test_case in range(1, int(input())+1):
    N, M = map(int, input().split())
    A, B = [], []
    t=Trie()
    cnt = 0

    for i in range(N):
        A.append(input())
    for i in range(M):
        B.append(input())
    
    for i in range(N):
        t.insert(A[i])
    for i in range(M):
        if t.search2(B[i]) == True:
            cnt+=1

    print("#{} {}".format(test_case, cnt))