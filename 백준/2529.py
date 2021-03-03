k = int(input())
sign = list(input().split())
check = [False] * 10
ans = []
# 함수 만드는 습관!

def sign_Check(num):
    for i in range(k):
        if sign[i] == '>':
            if num[i] > num[i+1]:
                continue
            else:
                return False
        if sign[i] == '<':
            if num[i] < num[i+1]:
                continue
            else:
                return False
    return True

def recur(index, strings):
    if index == k+1:
        if sign_Check(strings):
            ans.append(strings)
        return


    for i in range(10):
        if check[i]:
            continue

        check[i] = True
        recur(index+1,strings+str(i))
        check[i] = False
    



recur(0,'')
ans.sort()
print(ans[-1])
print(ans[0])