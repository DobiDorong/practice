# 튜플
# 형식: (값1, 값2, 값3, ...)
# - 좌표, (이름, 값)처럼 짝지어진 값을 하나로 묶을 때 사용
# sensor = ("모터온도",78)
# print(sensor)
# print(type(sensor))
# one = (78,)     # 값이 1개라도 ','표시해야 튜플로 인지 
# not_tuple = (78)
# print(type(one),type(not_tuple))

# 튜플 인덱싱, 슬라이싱
# s = ("모터 온도",78,"C")
# print(s[0],s[-1])
# readings = (78, 80, 79, 95, 77)
# print(readings[1:4])

# 튜플 언팩킹 - 한 번에 변수로 분리
# 형식: 변수1, 변수2 = 튜플     (변수 개수가 튜플 값 개수와 일치)
# name, value = sensor
# print(name, value)

# 실습1
# machine = ("모터온도", 78)
# print(machine[0],machine[1])
# name, value = machine
# print(name, value)


# 튜플 리스트 + 반복문(언패킹)
# - (이름, 값) 튜플들을 리스트로 모아 for 순회하면 이름, 값이 자동 분리
# sensors = [("모터온도",78), ("펌프압력",95), ("회전 속도",99)]
# for s in sensors:
    # print(s)
# for name, value in sensors:
#     # print(name,value)
#     if value > 90:
#         print(name,"경고")

# 중첩 튜플
# sensors = ("모터온도",78,(3,5))
# print(sensors[2][0])

# 튜플 리스트 정렬
# sensors = [(78,"모터온도"),(95,"베어링진동"),(32,"펌프압력")]
# hot = sorted(sensors,reverse=True)
# print(hot)

# 실습3
sensors = [("모터온도",78,(1,2)), ("펌프압력",95,(1,3)), ("회전 속도",1680,(2,3))]
under = []
for name, value, pos in sensors:
    x,y = pos
    # print(f'{name} 위치 x: {x} / y: {y}')
    if x <= 5:
        under.append(name)
print("x가 5 이하인 센서:",under[:])