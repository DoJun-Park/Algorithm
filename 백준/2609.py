# 유클리드 호제법 사용!!
# a,b의 최대공약수는 a%b와 b의 최대공약수와 같다.

A,B = map(int, input().split())
a,b=0,0

if B > A:
    tmp = A
    A = B
    B = tmp

a = A
b = B
while True:
    tmp = B
    B = A%B
    A = tmp

    if B == 0:
        print(A)
        print(A * int(a/A) * int(b/A))
        break
