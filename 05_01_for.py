# for 반복문
# for문 (range 이용한 반복)
# 형식: for 변수 in range(횟수):
# for i in range(5):
#     print("안녕하세요")

# for i in range(5):
#     print(i)        # 0 1 2 3 4
#     print('안녕하세요')

# # range(시작, 끝, 증가값)
# for i in range(1,10,2):     # 1 3 5 7 9
#     print(i)

# for i in range(5,0,-1):
#     print(i)                # 5 4 3 2 1

# 실습1
# n = int(input("반복 횟수: "))
# for i in range(1,n+1):
#     print(i, end=' ')
# print() 
# for i in range(2,n+1,2):
#     print(i, end=' ')
# print() 
# for i in range(n,0,-1):
#     print(i, end=' ')

# # 누적 변수 패턴 (합계, 갯수, 평균)
# total = 0
# for i in range(1,6):
#     total += i
# print('합계:', total)

# # 조건 만족하는 경우 세기
# count = 0
# for i in range(1,11):
#     if i> 5:
#         count += 1
# print("갯수:",count)

# # 평균
# total, count = 0, 0
# for i in range(1,6):
#     total += i
#     count += 1
# if count > 0:
#     print("평균:",total/count)

# 실습2
# total = 0
# n = int(input("값: "))
# for i in range(1,n+1):
#     total += i
# print("합:",total)

# enumerate: 순서 + 값을 함께 준다
# temps = [25, 26, 24]
# for idx, t in enumerate(temps):
#     print(idx + 1, "번째:",t)   # 1번째: 25...

# 중첩 반복문 (바깥 한 바퀴마다 안쪽이 처음부터 끝까지)
# for dan in range(2,10):
#     print(f'{dan}단')
#     for su in range(1,10):
#         print(f'{dan}x{su} = {dan*su}')
#     print("-------")

count = int(input('측정 횟수: '))
over_data = 0
for i in range(1,count+1):
    data = int(input(f'{i}번째 측정값: '))
    if data > 80:
        over_data += 1
print("초과 개수:",over_data)