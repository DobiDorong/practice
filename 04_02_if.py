# 조건문
# if 기본 구조 -콜론과 들여쓰기(코드 블록)
# 형식:
# if 조건식:
#   실행할 코드(들여쓰기)
# temp = 80
# if temp > 80:                  # 콜롬: 블록 시작 신호 
#     print("온도 주의")          
#     print("점검 요망")          # 들여쓰기 안 -> 조건 참일 때만 실행
# print("측정 종료")              # 들여쓰기 씉 -> 조건과 무관하게 항상 실행

# else - 조건이 거짓일 때
# 형식: 
# if 조건문:
#   참일 때 코드
# else:
#   거짓일 때 코드
# score = 55
# if score >= 60:
#     print("합격")
# else:
#     print("불합격")

# 실습1
# age = int(input("나이: "))
# if age >= 19:
#     print("성인입니다.")
# else:
#     print("미성년자입니다.")

# elif
# 형식:
# if ... elif... else (위에서부터 검사, 처음 참인 곳만 실행)

# 실습2
# score = int(input("점수: "))
# if score >= 90:
#     print("A")
# elif score >= 80:
#     print("B")
# elif score >= 70:
#     print("C")
# else:
#     print("F")

# 논리 연산자 and or not / 범위 조건
# temp =45
# print(temp >= 20 and temp <= 60)

# if 20 <= temp <= 60:
#     print("정상 범위")

# 실습3
# temp = int(input("온도: "))
# if temp > 80:
#     print("위험")
#    
# elif temp > 60:
#     print("주의")
# else:
#      print("정상")



# 실습 4
# ID = "dobi"
# PW = "dorong"
# id = input("아이디: ")
# pw = input("비밀번호: ")
# if ID == id and PW == pw:
#     print("성공")
# else:
#     print("실패")

# 실습 5
temp = int(input("온도: "))
vib = float(input("진동: "))
current = int(input("전류: "))
if temp > 80 or vib > 4.0:
    print("위험: 즉시 정지")
else:
    if current > 60 and temp > 70:
        print("주의: 부하 점검")
    elif vib > 2.5:
        print("주의: 진동 관찰")
    else:
        print('정상')

