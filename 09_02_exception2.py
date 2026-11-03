# try-except-else-finally
# - else: 예외가 하나도 안 났을 때만 실행
# - finally: 성공/실패 상관없이 무조건 마지막 실행

# text = "62.5"
# try:
#     temp = float(text)
# except ValueError:
#     print("변환 실패")
# else:
#     print("변환 성공:", temp)
# finally:
#     print("종료")


# 실습 1
# try:
#   f = open("data/09_ict_inspection.csv", "r", encoding="utf-8")
#   first = f.readline()
#   print(first.strip())    # 헤더
# except FileNotFoundError:
#   print("파일이 존재하지 않습니다")
# finally:
#   f.close()

# print("파일이 안전하게 닫힘")


# 실습 2, 3
# try:
#     with open("data/09_ict_inspection_dirty.csv", encoding="utf-8") as f:
#         rows = f.readlines()[1:]      # 슬라이싱 (헤더 빼려고)
# except FileNotFoundError:
#     rows = []

# total = 0.0
# skipped = 0
# for line in rows:
#     try:
#         total += float(line.split(",")[2])      # 측정값(2열)
#     except (ValueError, IndexError):
#         # 실습 2
#         # pass 
#         # 실습 3
#         skipped += 1
#         continue

# print("합계:", round(total, 1), "/건너뜀:", skipped)


# 실습 4
# names = [
#     "data/09_ict_inspection.csv",
#     "data/09_없는파일.csv",  # 중간에 배치
#     "data/09_ict_inspection_dirty.csv",
# ]
# done = 0
# for name in names:
#     # TODO: try에서 with open(name)
#     try:
#         with open(name, "r", encoding="utf-8") as f:
#             # TODO: 데이터 행 수 출력 / done 갱신
#             rows = f.readlines()[1:]
#         print("읽기 성공:", name, len(rows), "행")
#         done += 1
#     # TODO: FileNotFoundError 안내, continue
#     except FileNotFoundError:
#         print("건너뜀:", name)
#         continue
# print("처리한 파일:", done)

# # 실습5
# def check_value(text, lo = 0.0, hi=5000.0):
#     v = float(text)
#     if not (lo <= v <= hi):
#         raise ValueError(f'{v} 범위 밖')
#     return v

# for t in ["128.5", "결측", "-999"]:
#     try:
#         print("통과:", check_value(t))
#     except ValueError as e:
#         print("제외:", e)

