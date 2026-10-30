# 파일 입출력
# open()
# 형식: open(파일명, 모드, encoding)
# - 모드: r=읽기, w=새로 쓰기, a=이어쓰기
# - encoding = "utf-8" => 한글이 깨지지 않도록 하는 것
import os
import csv
FILE = "data/08_press.csv"   # 상수 설정 - 보통 다 대문자로 설정, 변하지 않는 값
ENCO = "utf-8"
# f = open(FILE, "r", encoding="utf-8")
# text = f.read()
# print(text)
# f.close     # 파일을 열고 난 후 닫기까지 해야함

# f = open(FILE, "r", encoding="utf-8")
# lines = f.readlines()
# print(type(lines),lines)
# f.close

# with open - 블록이 끝나면 자동 닫힘
# with open(FILE, "r", encoding="utf-8") as f:
#     for line in f:
#         print(line)

# write()
# with open("data/test.txt","w",encoding="utf-8") as f:
#     f.write("쓰기 테스트")

# 실습2
DATA = "data/test.txt"
with open(DATA,"w",encoding=ENCO) as f:
    f.write(f'AI를 활용한 데이터 분석\n기간: 2026.10 ~')
    f.write("안녕")
with open(DATA,"r",encoding=ENCO) as f:
    print(f.read())

# # 실습3
# with open(DATA,"a",encoding=ENCO) as f:
#     f.write("\n"+"수업 진행 방식: 비대면 / 대면")
# with open(DATA,"r",encoding=ENCO) as f:
#     print(f.read())

# csv.reader
# with open(FILE,"r",encoding=ENCO) as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(row)

# csv.writer
with open("data/08_summary.csv","w",encoding=ENCO,newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["설비ID", "상태"])     # 헤더
    writer.writerow(["PRESS-01", 1])
    writer.writerow(["PRESS-02", 1])

with open("data/08_summary.csv","r",encoding=ENCO) as f:
    print(f.read())
