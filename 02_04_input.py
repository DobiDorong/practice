# # 입력 (input)
# # 주의) 사용자 입력은 항상 "문자열"로 들어옴
# # 형식: 변수 = input("안내문구: ")
# name = input("이름: ")
# age = input("나이: ")

# print(name, age)

# # 형변환 - 정수: int(), 실수: float(), 문자열: str()
# # print(age+1)   TypeError
# print(int(age)+1)

# height = float("173.5")     #float() 실수 변환
# print(height,type(height))

# print("나이"+str(30))

# country = input("나라: ")
# city = input("도시: ")
# print(country, city)

# fir = int(input("숫자를 1개 골라주세요: "))
# sec = int(input("한 번 더 골라주세요: "))
# print(fir+sec, fir-sec, fir*sec,fir/sec, fir**sec)

# temp = float(input("현재 온도: "))
# temp_stand = temp>=35.5 and temp<= 37.5
# print(temp_stand)

korean = int(input("국어 점수: "))
math = int(input("수학 점수: "))
english = int(input("영어 점수: "))
avg = (korean+math+english)/3
print(avg)
print(korean>=80)
print(math>=80)
print(english>=80)