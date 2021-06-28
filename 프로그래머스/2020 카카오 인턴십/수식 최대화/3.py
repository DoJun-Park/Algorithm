def solution(n, k, cmd):
    answer = ''
    restore = []
    cnt = 0 #D와 U에서 몇 칸
    tmp_DC = []
    cur_index = k

    # dic = list(map(str,range(n)))
    
    tmp_dic = list(range(n))


    for i in range(n):
        tmp_dic[i] = i
    
    for i in cmd:
        if "D" in i:
            tmp_DC = i.split(' ')
            if cur_index + int(tmp_DC[1]) <= len(tmp_dic)-1:
                cur_index = cur_index + int(tmp_DC[1])

            else:
                cur_index = len(tmp_dic)-1
        
        elif "U" in i:
            tmp_DC = i.split(' ')
            if cur_index - int(tmp_DC[1]) >= 0:
                cur_index = cur_index - int(tmp_DC[1])

            else:
                cur_index = 0

        
        elif "Z" in i:
            a= 1
            tmp_val = tmp_dic[cur_index]

            tmp_dic.append(restore.pop())
            tmp_dic.sort()
            cur_index = tmp_dic.index(tmp_val)


        else: #제거
            restore.append(int(tmp_dic.pop(cur_index)))
            
            if cur_index == len(tmp_dic)-1:
                cur_index = cur_index-1
            else:
                cur_index = cur_index + 1


    for i in range(n):
        if i in tmp_dic:
            answer = answer + "O"
        else:
            answer = answer + "X"

    return answer