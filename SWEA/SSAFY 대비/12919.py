import sys
input = sys.stdin.readline

def dfs(s, t):
    if len(s) == len(t):
        if s==t:
            return 1
        else:
            return 0

    # A ... B 구조는 나올 수 없음 (1번 방법은 무조건 ... A 형식, 2번 방법은 무조건 B... 형식)
    if t[-1] == 'B':
        if t[0] != 'B':
            return 0
        # 무조건 2번 방법
        return dfs(s, t[:0:-1])

    else:
        # 무조건 1번 방법
        if t[0] == 'A':
            return dfs(s, t[:-1])
        else:
            # B ... A 는 1, 2 형식 모두 가능
            return dfs(s, t[:0:-1]) or dfs(s, t[:-1])


s = input().rstrip()
t = input().rstrip()
ans = dfs(s, t)
print(ans)