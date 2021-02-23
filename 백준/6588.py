MAX = 1000000

# 소수 판별 리스트
prime_list = [1] * (MAX+1)
prime_list[0] = prime_list[1] = False
prime_list[2] = True

#소수만 담는 list
prime_num=[] 

# 소수 찾아서 prime_num에 담기
for i in range(2,MAX+1):
    if prime_list[i]:
        prime_num.append(i)
        j=i
        while i*j <= MAX:
            prime_list[i*j] = False
            j +=1
# 입력값을 받아서 prime_num의 첫 원소부터 하나씩 뺐을때 빼고 나머지 값이 소수이면 그 두 수가 정답
# 나머지 값이 소수인지는 prime_list를 통해 확인
while True:
    i=int(input())
    if i == 0:
        break
    for n in prime_num:
        if  prime_list[i-n] == True:
            print("{} = {} + {}".format(i,n,i-n))
            break

