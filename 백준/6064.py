t = int(input())

loop = 0
while loop < t:
    Test_Case = list(map(int, input().split()))
    i = 0
    while i < 40000:
        year = Test_Case[0]*i + Test_Case[2]-1

        if Test_Case[3]-1 == year % Test_Case[1]:
            print(year+1)
            break
        i += 1
    else:
        print(-1)
    
    loop += 1




