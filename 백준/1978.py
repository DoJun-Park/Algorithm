n = input()
N_list = list(map(int, input().split()))
i = 0
prime_num_cnt = 0

while True:
    for j in range(1,N_list[i]+1):
        N_value = N_list[i]
        if N_value%2 == 0:
            continue
        else:
            for k in range(N_value-1, 2, -1):
                if N_value % k == 0:
                    continue

                prime_num_cnt += 1


print(prime_num_cnt)