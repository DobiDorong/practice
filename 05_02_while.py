# while - 조건이 참인 동안 반복
# 형식:
# while 조건식:         (조건이 거짓이 되는 순간 멈춤)
# for - '몇 번'이 정해졌을 때, while은 '언제 끝날지 모르지만 조건으로 멈출 때' 사용

# count = 1
# while count <= 3:
#     print(count)
#     count += 1
# 주의) 무한루프를 막으려면 (1)언젠간 거짓이 될 조건, (2)반복문 안에서 그 조건을 갱신
# 처음부터 조건이 거짓이면 한 번도 실행되지 않는다

# answer = 7
# insert = 0
# while answer != insert:
#     insert = int(input("답은 무엇입니까: "))
#     print("--바꿀 기회를 드리겠습니다--")
# print("정답입니다!")

# break - 반복 도중에 완전히 멈추기
# for i in range(1,11):
#     if i == 5:
#         print(i,'break')
#         break       # 5를 만나면 반복 즉시 종료
#     print(i)

# for i in range(1,7):
#     if i % 2 == 0:
#         continue
#     print(i)        # 1, 3, 5  

# detec = False
# count = int(input("횟수: "))
# for i in range(count):
#     temp = float(input("온도: "))
#     if temp > 80:
#         detec = True
#         break
# if detec:
#     print("발견")
# else:
#     print("이상 없음")
    

    