N = int(input())
N_cnt = len(str(N))
word_cnt = 0

word_chk = 1 #마지막 자릿수에서 계산할 갯수를 구하기 위해 ex) 137 -> 3자리 갯수 구하기 위해 137-100 에서 100을 이용하기 위한 값
word_standard = 9 # 각 자릿수에서의 전체 갯수 ex) 1의 자리 9개, 10의 자리 90개
word_mult = 1 # 한 자리 1개, 두 자리 2개

i = 1

while True:
    if i == N_cnt:
        word_cnt += word_mult * (N-word_chk + 1)
        print(word_cnt)
        break
    else:
        word_cnt += word_mult * word_standard
        word_mult +=1
        word_standard *= 10
        word_chk *= 10
        i += 1