while True:
    try:                    
        n = int(input())
        one_str = '1'
        Num_of_digit = 1
        while True:
            one_int = int(one_str)
            if one_int % n == 0:
                print(Num_of_digit)
                break
            else:
                one_str += '1'
                Num_of_digit +=1

    except:             ##EOF
        break



