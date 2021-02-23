N = int(input())
N_list = list(map(int, input().split()))


def chk_prime_num(x):
    if x <2:
        return False
    j=2
    while j*j <= x:
        if x%j == 0:
            return False
        j += 1

    return True

prime_num_cnt=0

for i in range(0,N):

    if chk_prime_num(N_list[i]):
        prime_num_cnt +=1

print(prime_num_cnt)
