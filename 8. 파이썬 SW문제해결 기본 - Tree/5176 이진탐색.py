# 다시 풀기

T = int(input())

def make_tree(n):
    global number
    # 배열이니까 배열크기 넘어가지 않도록
    if n <= N:
        # 왼쪽노드는 현재 인덱스의 2배
        make_tree(n * 2)
        # 더이상 못가면 값넣기
        tree[n] = number
        # 값 넣었으면 증가시키기
        number += 1
        # 우측 노드는 인덱스 2배 + 1
        make_tree(n * 2 + 1)

for tc in range(1, T + 1):
    N = int(input())

    tree = [0 for i in range(N + 1)]
    number = 1
    make_tree(1)
    print('#{} {} {}'.format(tc, tree[1], tree[N // 2]))
