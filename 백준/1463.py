N = int(input())
mem = [0] * (N+1)
mem[1] = 0

for i in range(2, N+1):
    mem[i] = mem[i-1] + 1

    if i % 2==0 and mem[i//2]+1 < mem[i]:
        mem[i] = mem[i//2]+1
    
    if i % 3==0 and mem[i//3]+1 < mem[i]:
        mem[i] = mem[i//3]+1

print(mem[N])







# 아래의 방법을 이용하면 메모리 초과

# import sys
# sys.setrecursionlimit(100000000) # 파이썬 최대 재귀 함수는 1000번이다. sys.setrecursionlimit()를 통해 제한풀 수 있다.

# N = int(input())
# mem = [0] * (N+1)

# def recur(num):
#     if num == 1:
#         return 0
    
#     if mem[num] != 0:
#         return mem[num] 
    
#     mem[num] = recur(num-1) +1 # 1을 뺐을 때의 경우

#     if num %2 ==0: # 2로 나눴을 경우
#         temp = recur(num//2) +1 
#         if temp < mem[num]:
#             mem[num] = temp
    
#     if num %3 ==0: # 3으로 나눴을 경우
#         temp = recur(num//3) +1
#         if temp < mem[num]:
#             mem[num] = temp

#     return mem[num]



# print(recur(N))