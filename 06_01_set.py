# set - 중복 자동 제거, 순서 없음
# 형식: {값1, 값2} 또는 set(리스트)
# - 빈 셋 set()
# logs = ["S01", "S02", "S01", "S03"]
# unique_logs = set(logs)
# print(unique_logs)		# {'S01', 'S02', 'S03'} set은 순서가 없어서 인덱싱 불가
# print(sorted(unique_logs))	# ['S01', 'S02','S03'] 

# add - 값 추가 / in - 포함을 확인
# alerts = {"S01", "S02"}
# alerts.add("S03")
# print(alerts)		# {'S02', 'S03', 'S01'}
# alerts.add("S01")
# print(alerts)		# {'S02', 'S03', 'S01'} 이미 있는 값은 안들어감
# print("S02" in alerts)	# True

# 실습4
# sensors = ['pump_A', 'pump_B', 'pump_C', 'pump_B']
# clear_sensors = set(sensors)
# print(sorted(clear_sensors))
# print("설비 종류 수:", len(clear_sensors))

# 집합 연산 - union(합산) / intersection(중복) / difference(한쪽만)
# line_a = {"S01", "S02", "S03"}
# line_b = {"S03", "S04"}
# all_s = line_a.union(line_b)
# common = line_a.intersection(line_b)
# differ = line_a.difference(line_b)
# print(all_s)
# print(common)
# print(differ)

# 실습5
# line_a = {"S01", "S02", "S03"}
# line_b = {"S03", "S04"}
# all_s = line_a.union(line_b)
# common = line_a.intersection(line_b)
# differ_a = line_a.difference(line_b)
# differ_b = line_b.difference(line_a)
# print("전체:",all_s)
# print("공통:",common)
# print("A만:",differ_a)
# print("B만:",differ_b)

# 실습6
before = {"S01", "S02", "S03"}
today = {"S03", "S04","S05"}
new = today.difference(before)
same = today.intersection(before)
print("신규 이상:",new)
print("지속 이상:",same)