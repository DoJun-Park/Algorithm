M,N = map(int, input().split())

MAX=1000000
prime_list = [1] * (MAX+1)

# 소수이면 True, 아니면 False
prime_list[0]=prime_list[1]=False


for i in range(2,N+1):
    if prime_list[i]:
        j=i
        while i*j <=N:
            prime_list[i*j] = False
            j +=1


for i in range(M,N+1):
    if prime_list[i] == True:
        print(i)
