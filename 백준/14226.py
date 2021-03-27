from collections import deque

S = int(input())
emo = [[0] * (S+1) for _ in range(S+1)]
screen = 1 #화면에 있는 이모티콘 갯수
clip = 0 # 클립보드에 있는 이모티콘 갯수
q = deque()
q.append((screen,clip))
emo[screen][clip] = 0

while q:
    screen, clip = q.popleft()

    if emo[screen][screen] == 0:
        emo[screen][screen] = emo[screen][clip] + 1
        q.append((screen,screen))
    
    if screen + clip <= S and emo[screen + clip][clip] == 0:
        emo[screen+clip][clip] = emo[screen][clip] + 1
        q.append((screen+clip, clip))
    
    if screen >= 1 and emo[screen-1][clip] == 0:
        emo[screen-1][clip] = emo[screen][clip] + 1
        q.append((screen-1, clip))
    
ans = 0

for i in range(S+1):
    if emo[S][i] != 0:
        if ans == 0 or ans > emo[S][i] :
            ans = emo[S][i]
print(ans)

    