n = int(input())

fibo_list = [0,1]

if n>1:
    for i in range(2,n+1):
        fibo_num = fibo_list[i-1] + fibo_list[i-2]
        fibo_list.append(fibo_num)

print(fibo_list[n])