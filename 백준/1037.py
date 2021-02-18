N= int(input())
list_divisor = list(map(int, input().split()))

A = min(list_divisor) * max(list_divisor)

print(A)