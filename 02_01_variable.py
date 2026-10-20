# 변수와 할당 - 값에 이름 붙이기
# 형식 : 변수이름 = 값 <- 오른쪽 값을 왼쪽 이름에 "저장"하라는 명령
temp = 25
name = "센세 A"
count = 3

print(temp)
print("temp")
x = 10
x = x + 5
print(x) 

# 변수 이름 규칙
# 형식 : 영문자, 숫자, 밑줄 사용 가능 / 숫자로 시작 불가/ 공백 불가
sensor_count = 3    # snake_case
temp2 = 10          # 숫자 사용 가능 (숫자로 시작 불가)
# 2temp = 2         # SyntaxError: invalid decimal literal

# 대소문자 구분, 재할당
temp = 25
Temp = 100
print(temp, Temp)
# 재할당: 마지막에 저장한 값만 남음
score = 10
score = 20
print(score)




