N = int(input())

for i in range(N):
    correct_false_list = list(input())
    sequence_num = 0
    add_num = 1
    score = 0

    for j in range(len(correct_false_list)):
        if correct_false_list[j] == 'O':
            if sequence_num == 1:
                add_num = add_num+1

            score = score + add_num
            sequence_num = 1
                
        else:
            sequence_num = 0
            add_num = 1

    print(score)
