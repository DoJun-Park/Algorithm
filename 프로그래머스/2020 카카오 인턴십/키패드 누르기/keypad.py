def solution(numbers, hand):

    keypad = {1: (0, 0), 2: (0, 1), 3: (0, 2),
              4: (1, 0), 5: (1, 1), 6: (1, 2),
              7: (2, 0), 8: (2, 1), 9: (2, 2),
              '*': (3, 0), 0: (3, 1), '#': (3, 2)}


    current_left_key = '*' #왼손 시작 *
    current_right_key = '#' #오른손 시작 #

    left_possible_key = [1,4,7]
    right_possible_key = [3,6,9]

    ans='' # 정답

    # x = [0,0,-1,1] #상하좌우
    # y = [1,-1,0,0] #상하좌우



    which_hand = False #왼손잡이 인지 오른손잡이 인지 
    if hand == 'right':
        which_hand = True  # 오른손잡이 - True

    for i in numbers:
        if i in left_possible_key:
            current_left_key = i
            ans = ans + 'L'
        
            
        elif i in right_possible_key:
            current_right_key = i
            ans = ans + 'R'

        else:

            x,y = 0,1
            dist_left = abs(keypad[current_left_key][x] - keypad[i][x]) + abs(keypad[current_left_key][y] - keypad[i][y])
            dist_right = abs(keypad[current_right_key][x] - keypad[i][x]) + abs(keypad[current_right_key][y] - keypad[i][y])

            if dist_left == dist_right:
                if which_hand:
                    ans = ans + 'R'
                    current_right_key = i
                else:
                    ans = ans + 'L'
                    current_left_key = i
            
            else:
                if dist_left > dist_right:
                    ans = ans + 'R'
                    current_right_key = i
                else:
                    ans = ans + 'L'
                    current_left_key = i

    return ans

        


