number = 20
greeting = '안녕하세요'
place = "부산광역시"

print(number, '번 손님', greeting, ' 여기는 ', place, '입니다')

base = '{}번 손님, {}에 오신 것을 {}!'
new_way = base.format(number, place, greeting)


print(base)
print(new_way)