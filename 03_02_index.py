# 인덱싱 - 위치 번호로 글자를 하나 꺼내기
# 형식 : 문자[번호]     (첫 글자 = 0번)

# word ='PYTHON'
# print(word[0], word[3], word[5])
# # 음수 인덱스: 뒤에서부터 -1, -2, ...
# print(word[-1], word[-2], word[-5])

# print(word[6])   # IndexError: string index out of range

# word = 'SIGNAL'
# # print(word[0], word[2],word[5])
# print(word[-1],'/', word[-2])

# 슬라이싱 - 구간으로 잘라내기
# 형식: 문자열[시작:끝] (시작은 포함, 끝 제외)
#print(word[0:3], word[2:5])
# 생략 가능
# - 시작 생략 = 처음부터 (0번부터)
# - 끝 생략 = 끝까지
# - 둘 다 생략 = 전체
# print(word[:4])     # 0, 1, 2, 3번
# print(word[2:])     # 2, 3, 4, 5번
# print(word[:])      # 전체
# # 음수
# print(word[-6:])
# print(word[-3:])
# print(word[:-1])

# word = 'temp_sensor'
# print(word[:4])
# print(word[5:])

# word = 'sensor_01'
# print(word[-2:])

# step 간격 주기
# 형식: 문자열[시작:끝:간격]
# print(word[::2])
# print(word[1::3])

word = 'SiGNAL'
# print(word[::2])
print(word[::-1])