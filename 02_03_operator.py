# 연산자
# - 산술, 비교, 논리 연산자

# 산술 연산자
# 형식: +, -, *, /, //(몫), %(나머지), **(거듭제곱)

# 우선순위
# - 곱셈, 나눗셈 등이 우선, 괄호를 사용하면 우선순위를 바꿀 수 있음

# 복합 할당
# 형식: +=, -=, *=, /=
# # 예시: score += 10 <-> score = score + 10
# score = 100
# score += 10
# print(score) 

# # 문자열 연산
# # +, * 가능
# print("안녕" + "하세요") # 안녕하세요
# print("-" * 8)         # --------
# # 자료형이 같은 것끼리만 연산 가능, 숫자와 문자끼리 연산 불가능

# a, b = 17, 5
# print(a+b, a-b, a*b, a/b, a//b, a%b, a**b)

# width, length, height = 8, 8, 9
# avg = round((width + length + height) / 3, 3)
# ext = width * length
# vol = width * length * height
# print(avg, ext, vol)

# # 비교 연산자
# print(3==3, 3!=3, 3>5, 3<5, 6>=2, 5<=2)

# #논리 연산자
# temp = 85
# temp_stand = temp >= 60 and temp <= 90
# press = 5
# press_stand = press >= 3 and press <= 7
# print("온도정상", temp_stand)
# print("압력정상", press_stand)
# print("모두정상", temp_stand and press_stand)

# stock = 100
# print(stock)
# stock += 50 
# print(stock)
# stock -= 30
# print(stock)
# stock +=5
# print(stock)

# pro = 500
# err = 23
# err_per = 23/500 *100
# oper_time = 21/24*100
# print("불량률", err_per,"%", "가동률", oper_time,"%")
print(500//60,"시간", 500%60,"분")