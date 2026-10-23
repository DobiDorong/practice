# 리스트
# 형식: 이름 = [값1, 값2, ...]
# - 리스트는 여러 값을 '순서대로' 한 이름에 담는다.

# temps = [25, 26, 24, 27, 26]
# machines = ['펌프', '모터', '압축기']
# mixed = ['펌프', 87, True] # -> 다른 형태여도 같이 담을 수 있다.
# empty =[]
# print(temps)
# print(len(temps))
# print(empty)
# print(len(empty))

# temps = [22, 34, 27, 52, 44, 23]
# print(temps[0], temps[2], temps[-1])

# temps = [22, 34, 27, 52, 44, 23, 56, 32, 86, 74]

# print(f'{temps[:3]} / {temps[-3:]} / {len(temps[:3])}')

# prod = [121, 222, 426, 128, 401]
# value1, value2 = prod[0], prod[-1]
# add = value1+value2
# print(add)
# print(add/2)

# data = [1, 3, 4, 6, 7, 11, 14, 17, 22, 54, 38, 96]
# first = data[:6]
# print(first)
# second = data[-6:]
# print(second)
# print(len(first), len(second))

# 값 바꾸기 / in 존재 확인
# 형식: 리스트[번호] = 새 값 / 값 in 리스트
# nums = [25, 26, 24, 28, 27]
# nums[2] = 99
# print(nums)
# machines = ['펌프', '모터', '압축기']
# print("모터" in machines)

# 값 추가 - append, insert, extend
# 형식: 리스트.append(값) / 리스트.insert(위치, 값) / 리스트.extend(다른 리스트)
# data = [25, 26, 27, 28]
# data.append(28)
# data.insert(1,99)
# data.extend([30,31])
# print(data)

# temps = [25, 26, 24, 28, 27, 240]
# print(240 in temps)
# temps[temps.index(240)] = 24
# print(temps)
# print(240 in temps)

# data = []
# data.append(30)
# data.insert(0,28)
# data.extend([31,32])
# print(data)

# 값 삭제 - remove, pop, del
# 형식: 리스트.remove(값) / 꺼낸 값 = 리스트.pop(위치) / del 리스트[위치]
# d = [25, 26, 24, 28, 27]
# d.remove(24)
# print(d)
# p = d.pop(1)
# print(d, p)
# del d[2]
# print(d)

# 정렬, 탐색 - sort, reverse / count, index
# 형식: 리스트.sort() .reverse()    .count(값)  .index(값)
# l = [27, 24, 30, 22, 26]
# l.sort()
# print(l)
# l.sort(reverse=True)
# print(l)
# l.reverse()
# print(l)
# print(l.count(24))
# print(l.index(24))

# temps = [25, 26, 999, 24, 28, 26]
# temps.remove(999)
# print(temps)
# data = temps.pop(1)
# print(data)
# del temps[0]
# print(temps)

temps = [22, 26, 24, 29, 32, 22, 28]
temps.sort()
print(temps)
temps.reverse()
print(temps)
print(temps.count(22), temps.index(22))