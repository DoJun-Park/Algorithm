L,C = map(int, input().split())
sorted_alpa = sorted(list(input().split()), reverse=False)
chk_list = [False] * (C+1)


def vowel_consonant_cnt(password): #암호에서 자음, 모음 갯수 확인
    vowel,consonant = 0,0

    for i in password:
        if i in 'aeiou':
            vowel += 1
        else: 
            consonant += 1
    
    if consonant >= 2 and vowel >= 1 :
        return True
    else:
        return False

def recur(index,password):
    if len(password) == L:
        if vowel_consonant_cnt(password):
            print(password)
        return 0
    

    for i in range (index, C):
        if chk_list[i+1]:
            continue
        else:
            temp_password = password
            password += sorted_alpa[i]
            chk_list[i+1] = True
            recur(i+1,password)
            password = temp_password
            chk_list[i+1] = False
    



recur(0,'')