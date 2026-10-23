# 문자열 연산과 검색
# - 문자열 연결(+), 반복(*)

# len() - 글자 수
# # 형식: len(문자열)
# print(len('PYTHON'))    # 6 
# print(len('AI 분석'))    # 5(공백도 글자 수에 포함)
# print(len(''))          # 0(빈 문자열) 

# in / not in - 포함 / 불포함 여부 (결과 bool)
# 형식: '찾을 것' in 문자열
# print('고장' in '설비 고장 발생')
# print('정상' not in '고장 발생')

# # count
# # 형식: 문자열.count('확인하고 싶은 것') -> 개수
# print('banana'.count('a'))

# # find
# # 형식: 문자열.find('x') -> 처음 나오는 위치
# print('banana'.find('a'))   # 1
# print('banana'.find('t'))   # 찾고자 하는 값이 없으면 -1

# # 실습1
# num = '01012345678'
# print(len(num))

# 실습2
# print('고장' in '설비 고장 발생', '정상' in '설비 고장 발생')

# # 실습3
# name = 'sensor-01-temp'
# print(name.count('-'))

# 실습4
# data = 'temp_2024'
# print(data.find('_'), data.find('y'))

# index 
# 주의) 값이 없으면 오류가 뜸
# email = 'hong@company.com'
# at = email.index('@')
# print(at)
# print(email[:at])

# startswith / endswith
# # 형식: 문자열.startswith('x') -> bool
# print('EQP-001'.startswith('EQP'))
# print('cmapss.csv'.endswith('csv'))

# name = 'sensor_log.csv'
# start = name.startswith('sensor')
# end = name.endswith('csv')
# print(start,end)

label1 = 'WARNING'
label2 = 'warning'
print(label1==label2)
