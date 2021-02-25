sum = 0
N = []

for i in range(9):
    N.append(int(input()))
    sum += N[i]

i=0

while i < 8:
    j = i+1
    for j in range(j,9):
        # print("{}와 {}".format(i,j))
        if (sum-N[i]-N[j]) == 100:
            N[i] = 100
            N[j] = 100
            i=8
            break
    i += 1


N.sort()

for i in range(7):
    print(N[i])

