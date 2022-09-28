import sys
input = sys.stdin.readline

K , n_slang = map(int, input().split())
slangs = [input().strip() for _ in range(n_slang)]
chat = input().strip()

def match(slang, word):
    n = len(slang)
    m = len(word)
    dy = [[False for _ in range(m+1)] for _ in range(n+1)]
    dy[0][0] = True

    for i in range(1, n+1):
        for j in range(1, m+1):
            if slang[i-1] == word[j-1]:
                dy[i][j] |= dy[i-1][j-1]
            if word[j-1] == '.':
                for k in range(1, K+1):
                    if i - k >= 0:
                        dy[i][j] |= dy[i-k][j-1]

    return dy[n][m]

ans = []
for word in chat.split():
    if any(match(slang, word) for slang in slangs):
        ans.append('#' * len(word))
    else:
        ans.append(word)

print(*ans)
