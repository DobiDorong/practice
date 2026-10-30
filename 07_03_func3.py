# 함수 설계와 활용

# 기본값 인자
# 형식:
# def 함수(매개변수-필수, 선택 = 기본값)

# 거의 항상 같은 값을 매번 적는 번거로움을 줄임, 필요할 때만 덮어쓴다.
# def report(name,value,unit="도"):
#     print(f'{name}: {value}{unit}')
# report("압축기1",75.3)
# report("펌프1",7.2, "bar")

# def temp(a,b="정상"):
#     print(a,"->",b)
# temp(78)
# temp(95, "경고")
# # temp(a =50, "경고")
# temp(a =50, b="경고")

# # 지역 변수와 범위(스코프)
# # - 함수 안의 변수, 함수 바깥 변수를 읽을 수 있지만, 바깥에서는 함수 안 지역변수를 읽을 수 없다.
# def calc():
#     result = 10+5   # 지역변수
#     return result   # 밖에서 사용하려면 return으로 내보내야한다.

# print(calc())

# x = 10
# def change():
#     x = 20 # 함수 안 x (별개)
# change()
# print(x) # 출력: 10


# 실습2
# def calc():
#     value = 30
#     return value
# print(calc())
# # print(value)

# 함수 조합 (함수 설계: 입력/처리/출력)
# def get_avg(values):
#     return sum(values)/len(values)
# def judge(avg, limit=90):
#     if avg > limit:
#         return "위험"
#     else:
#         return "정상"
# temps = [78, 86, 92]
# avg = get_avg(temps)
# print("평균",round(avg,1),"->", judge(avg))

