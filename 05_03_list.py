# temps = [27, 24, 19, 31, 29, 32]
# for t in temps:
#     if t >= 30:
#         print("고온:",t)

# time = [3,7,5,8,1,2,9,12,10]
# for t in time:
#     if t>=5 and t<=10:
#         print(t)

# 최대, 최소 
# temps = [25,32,28,36,27,31]
# biggest = temps[0]
# for t in temps:
#     if t > biggest:
#         biggest = t
# print(biggest)

# # 빈 리스트 채우기
# doubled =[]
# for t in temps:
#     doubled.append(t*2)
# print(doubled)

# 실습3
# temps = [27,21,29,31,37,32]
# total = 0
# count = 0
# for t in temps:
#     if t > 30:
#         total += t
#         count += 1
# print(total, count)
# print(f'고온 평균: {total/count:.2f}')

# 실습4
# temps = [27,21,29,31,37,32]
# over_temps = []
# for t in temps:
#     if t > 30:
#         over_temps.append(t)
# print(f'{over_temps} / {len(over_temps)}개')
# print(temps)

# 실습5
# temps = [27,21,29,31,37,32]
# F = []
# for t in temps:
#     f = round(t*1.8+32,1)
#     F.append(f)
# print(F)

# 중첩 리스트 - 리스트 안에 리스트
# - 표(행,열)처럼 한 줄에 여러 값이 묶인 데이터. 바깥 반복은 '행;, 안쪽 인덱스로 '열'
# rows = [["펌프",25],["모터",32],["압축기",28]]
# for row in rows:
#     print(row[0],"온도",row[1])

# 실습6
temps = [27,21,29,30,37,32]
over = []
value = 0
over_value = 0
for t in temps:
    value += t
    if t > 30:
        over.append(t)
        over_value += t
print("전체 평균 온도:",value/len(temps))
print("고온 개수:",len(over))
print("초과 온도 평균:",over_value/len(over))
