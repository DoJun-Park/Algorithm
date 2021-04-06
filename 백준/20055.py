N,K = map(int, input().split())
a = list(map(int, input().split()))
box = [False] * (2*N)
zero = 0
t = 1

while True:
    a = a[-1:] + box[:-1]
    box = box[-1:] + box[:-1]

    if box[N-1]:
        box[N-1] = False
    for i in range(N-2, -1, -1):
        if box[i]:
            if box[i+1] == False and a[i+1] > 0:
                box[i+1]= True
                box[i] = False
                a[i+1] -= 1
                if a[i+1] == 0:
                    zero += 1
    if box[N-1]:
        box[N-1] = False
    if a[0] > 0 :
        box[0] = True
        a[0] -= 1
        if a[0] == 0:
            zero += 1
    if zero >= K:
        print(t)
        break

    t+=1
        