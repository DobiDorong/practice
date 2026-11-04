import numpy as np

# 리스트 vs 배열
# 1) 리스트
# - 서로 다른 자료형도 같이 존재 가능
# - 계산이 느리고 반복문을 붙여야 한다
# list = [70, 72, 75]
# print(list*2)
# print([v*2 for v in list])

# 2) 배열
# - 같은 자료형만 존재 가능
# - 계산이 빠르고 반복문 없이도 가능

# temp = np.array([70, 72, 75])
# print(temp)     # [70 72 75]
# print(temp+2)   # [72 74 77]

# # 튜플도 배열 만들기
# print(np.array((1, 2, 3)))   # [1 2 3]

# 실습1
# temps = np.array([70, 73, 76, 72, 79, 80])
# print(temps)
# temps_array = temps*1.8+32
# print(temps_array)

# 배열 생성
# np.arange(시작, 끝, 간격) : 연속된 정수로 이루어진 배열 생성
# - 끝값은 포함되지 않음
# print(np.arange(5))     # [0 1 2 3 4]
# print(np.arange(0, 10, 2))      #[0 2 4 6 8]

# np.linspace(시작, 끝, 개수) : 균등 분할
# - 시작과 끝을 포함
# print(np.linspace(0, 1, 5))     # [0.   0.25 0.5  0.75 1.  ]
# print(np.linspace(0, 10, 5))    # [ 0.   2.5  5.   7.5 10. ]

# 실습2
# print(np.linspace(0,70,8))

# 실습3
# print(np.arange(0,40,5))

# 배열 속성
# - ndim, shape, size, dtype
# - 속성은 괄호 없이 사용

# a = np.array([1,2,3])
# b = np.array([[1,2,3],[4,5,6]])
# print("dim:", a.ndim, b.ndim)   # dim: 1 2
# print("shape:", a.shape, b.shape)   # shape: (3,) (2, 3)
# print("size:", a.size, b.size)  # size: 3 6
# print("dtype:", a.dtype, b.dtype)  # dtype: int64 float64

# 실습4
time = np.array([[70, 35], [80, 40], [73, 42], [75, 38]] )
# print(time)
# print(time.ndim)
# print(time.shape)
# a,b = time.shape
# print(time.size)
# print(a*b == time.size)

# 실습5
# cur = np.array([15.78, 16.02, 15.56, 15.98])
# print(cur.dtype)
# cur_int = cur.astype(np.int64)
# print(cur_int)

# reshpae() 로 형태 바꾸기
# - '-1'을 사용 시 자동 계산 (행 또는 열에 한 번만 사용)
# c = np.arange(12)
# print(c.reshape(3,4))
#[[ 0  1  2  3]
# [ 4  5  6  7]
# [ 8  9 10 11]]

# flatten() -> 1차원 배열로 변환
b3 = np.array([[1,2,3],[4,5,6]])
# print(b3.flatten())   # [1 2 3 4 5 6]

# 실습6
# cycle = np.array([16, 18, 13, 15, 17, 20, 12, 13, 16, 21, 11, 14])
# cycle_re = cycle.reshape(3,4)
# print(cycle_re)

# 실습7
# data = np.array([70, 16.8, 3500, 73, 15.9, 3480, 77, 18, 3700, 81, 15.1, 3400])
# data_1 = data.reshape(4,3)
# data_fla = data_1.flatten()
# print(data_1)
# print(data_fla)

