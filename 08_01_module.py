# 모듈 / 패키지 / 라이브러리
# - 모듈: 기능을 모아둔 .py 파일 하나
# - 패키지: 모듈을 모아둔 폴더
#- 라이브러리: 위에 사항들을 통칭

# import 방식
# 형식: import 모듈
# import math     # math 라는 모듈을 통째로 불러옴
# print(math.sqrt(16))    #4.0

# from math import sqrt, ceil     # 일부만 불러옴 -> 모듈명 없이 바로 사용
# print(sqrt(16),ceil(4.2))

# import math as m
# print(m.sqrt(16))

# 실습1
# import math
# print(math.sqrt(16), math.ceil(4.3))
# from math import sqrt, ceil
# print(sqrt(16),ceil(4.3))
# import math as m
# print(m.sqrt(16),m.ceil(4.3))

#  표준 라이브러리 - math / random / datetime
# - 파이썬 설치 시 함께 깔리는 검증된 모듈들
# import random
# import datetime

# print(random.randint(1,100))
# print(datetime.datetime.now())

# 실습2
# import random
# a = random.randint(1,81)
# print(a)
# import math
# print(math.sqrt(a))

# 경로와 os 모듈
# - 파일을 다루려면 어디에 있는지 경로를 알아야 한다
# 1) 절대 경로
#   - 최상위부터 전체 주소
# 2) 상대 경로
#   - 지금 실행 중인 위치를 기준으로 한 주소

# import os
# print("현재 실행 위치(절대경로):",os.getcwd())

# # 폴더 유무 확인
# print(os.path.exists("data"))   # 폴더의 존재 유무를 알려줌 True

# # 폴더 목록 확인
# files = os.listdir("data")
# print(files)

# path = os.path.join("data",'08_press_13_261029_3.csv')
# print(path)

# # 실습3
# import os
# print("현재 경로: ", os.getcwd())
# list = os.listdir("data")
# for name in list:
#     print(name) 
# for file in list:
#     if file.endswith(".csv"):
#         print(file)

# # 폴더명 + 파일명 -> 경로
# # # 실습4
# import os
# path = os.path.join("data", "08_press_13_261029_3.csv")
# print(os.path.exists(path))
# if os.path.exists(path):
#     print("파일 있음")
# else:
#     print("파일 없음")

# # 실습5
# import os, datetime
# count = len(os.listdir("data"))
# print("파일 수:",count,"개")
# time = datetime.datetime.now()
# print(f'파일 수: {count}개, 점검 시각 {time}')

# 실습6
import os
list = os.listdir("data")
csv_list =[]
for name in list:
    if name.endswith(".csv"):
        csv_list.append(name)

print("[CSV]")
for name in csv_list:
    path = os.path.join("data",name)       
    print(" -",name)
