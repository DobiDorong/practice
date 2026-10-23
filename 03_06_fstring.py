# f-string - 문자열 안에 변수를 바로 끼우기
# 형식: f'abc{변수}qfd'

# name = '홍길동'
# age = 25
# print(f'{name}님은 {age}살 입니다.')

# 숫자도 str 변환 없이 바로 들어감
# print(f'온도: {25.5}')
# # 중괄호 안에 계산식 가능
# hours = 3
# print(f'{hours*60}분')

# 소수점 자리수 조정
# 형식: {값(변수):.2f} -> 소수점 둘째 자리까지 (자동 반올림)
# value = 25.487256
# print(f'측정값: {value:.2f}')
# print(f'측정값: {value:.1f}')

# name = '설비 PUMP_A'
# temp = 87
# print(f'{name}, 온도 {temp}도')

# score1 = 90
# score2 = 91
# score3 = 83
# print(f'평균 점수: {(score1+score2+score3)/3}')

# value = 87.456
# print(f"{value:.1f} / {value:.2f}")

label = ' 5, sensor_2 , WARNING , 0.78912 '
# label = label.strip().split(',')
# label = [label[0].strip(),label[1].strip(),label[2].strip(),float(label[3].strip())]
# print(f'[센서{label[1]}] 상태 {label[2].lower()}, 측정값{label[3]:.2f}')

label = label.replace(' ','').split(',')
label[2] = label[2].lower()
label[3] = float(label[3])
print(label)
print(f'[센서 {label[1]}] 상태 {label[2]}, 측정값 {label[3]:.2f}')

label = ' 5, sensor_2 , WARNING , 0.78912 '
label = label.strip().split(',')
part = label[1].strip()
status = label[2].strip().lower()
value = float(label[3].strip())
print(f'[센서 {part}] 상태 {status}, 측정값{value:.2f}')
