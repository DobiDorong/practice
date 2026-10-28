# 딕셔너리
# 형식: {키:값, 키:값} - 키는 문자열, 
#  리스트는 번호(인덱스)로 찾지만 딕셔너리는 이름(키)으로 찾는다.

# sensors = {"모터온도":78, "진동":0.5}
# print(sensors)
# print(sensors["모터온도"])	# 78
# print(type(sensors))		# <class 'dict'>
# print(sensors["유량"])	# keyerror -> 없는 키를 조회 시 에러

# 추가/ 수정 / 삭제
# 형식: 딕셔너리[키] = 값 (없는 키는 추가, 있는 키는 수정)
# 형식: (삭제) del 딕셔너리[키]

# sensors["펌프압력"] = 95	# 추가
# sensors["모터온도"] = 80	# 수정
# del sensors["진동"]		# 삭제 (없는 키를 삭제할 경우 오류 발생)
# print(sensors)		# {'모터온동': 80, '펌프압력': 95}

# get / in
# 형식: 딕셔너리.get(키, 기본값) / 키 in 딕셔너리
# print(sensors.get("유량"))	# None
# print(sensors.get("유량", 0))	# 0
# print("모터온도" in sensors)	# True (키만 포함 여부 확인 가능)
# print(80 in sensors)		# False (값은 검색이 안됨)

# 실습1
# sensors = {"모터온도": 95, "회전수": 1950, "진동": 4.5}
# print(sensors["진동"])
# sensors["회전수"] = 1780
# sensors["압력"] = 130
# print(sensors)
# print(sensors.get("작동 시간", 0))
# print("압력" in sensors)

# keys / values
# sensors = {"모터온도":78,"진동":0.5}
# print(list(sensors.keys()))
# print(list(sensors.values()))
# avg = sum(sensors.values()) / len(sensors)
# print(avg)

# for name, value in sensors.items():
# 	print(name,value)

# for k in sensors.keys()
# for v in sensors.values()

# update - 여러 항목 한 번에 갱신(키가 있으면 수정, 없으면 추가)
# d = {"온도":78}
# d.update({"온도":85,"압력":75})

# 실습2
# sensors = {"온도": 98,"압력": 65}
# new = {"온도": 78,"회전수":1820}
# sensors.update(new)
# print(sensors)
# del sensors["압력"]
# print("센서 수:", len(sensors))

# 실습3
# temp_sensors = {"센서A":86, "센서B":78,"센서C":83}
# avg = sum(temp_sensors.values())/len(temp_sensors)
# print("평균:",round(avg,1))
# max = 0
# n = ""
# for name, value in temp_sensors.items():
# 	if value > max:
# 		max = value
# 		n = name
# print("최대값 센서:",n,max)

# zip : 센서명 - 값 매핑하기
# names = ["온도","진동","압력"]
# values = [78, 0.5, 95]
# sensors = dict(zip(names, values))
# print(sensors)

# 딕셔너리의 값에 리스트/딕셔너리 - 중첩 딕셔너리
# plant = {
# 	"1번모터":{"온도": 78, "상태":"정상"},
# 	"2번모터":{"압력": 95, "상태":"경고"}
# }
# print(plant["2번모터"]["압력"])		# 95

# 실습 4
# names = ["온도","진동","압력"]
# values = [78, 0.5, 95]
# sensors = dict(zip(names, values))
# print(sensors)
# for name, value in sensors.items():
# 	print(name,value)

# 실습5
# temps = {"온도":90,"진동":3.2,"압력":89}
# limits = {"온도":82,"진동":3.8,"압력":94}
# over = []
# for name, value in temps.items():
# 	if value > limits[name]:
# 		over.append(name)
# print("경고 센서:",over)

# 실습6
# machine = {"1번펌프":{"온도":78,"압력": 85,"진동":4.5},"2번펌프":{"온도":84,"압력": 95,"진동":4.0}}
# limits = {"온도":80,"압력": 90,"진동":5.0}
# print(machine["2번펌프"]["압력"])
# for name,state in machine.items():
# 	for sensor,value in state.items():
# 		if value > limits[sensor]:
# 			print(name,sensor,"점검 필요")


# 실습7
# data = ["온도,78","압력,95.0","진동,0.5"]
# sensors = {}
# for t in data:
# 	name, value = t.split(",")
# 	sensors[name] = float(value)
# print(sensors)

# 실습8
temps = {"온도":90,"진동":4.7,"압력":89}
limits = {"온도":82,"진동":3.8,"압력":94}
avg = sum(temps.values())/len(temps)
print("평균:",round(avg,1))
s = set()
for name,value in temps.items():
	if value > limits[name]:
		s.add(name)
print("위험 센서:",sorted(s))