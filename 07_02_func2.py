# 매개변수와 반환값

# 매가변수와 인자
# 형식:
# def 함수이름(매개변수):

# 호출
# 함수이름(인자)

# 실습1
# def check(name):
#     print(name+" 점검을 시작합니다. ")
# check("압축기A")      # "압축기A" = 인자
# check("펌프1")
# check()

# 실습2
# def state(name,temp):
#     print(name,temp,"도")
# state("모터",78)
# state("펌프",92)
# state(92,"펌프")

# 실습3
# def state(name,temp):
#     print(name,temp,"도")
# state(temp=78,name="모터")
# state(name="모터",temp=78)
# state("모터",temp=78)
# # state(temp=78,"모터") # SyntaxError: positional argument follows keyword argument

# return
# - print: 사람이 확인할 수 있게 출력 / return : 값을 프로그램에게 돌려줘서 이어 쓸 수 있게 해준다.
# def add(a, b):
#     return a + b   
#     print("실행 안됨") # return을 만나면 즉시 함수가 종료됨 -> 그 아래 코드는 실행 X
    
# total = add(3, 4)
# print(total)

# 실습4
# def calc(a,b,c):
#     return a*b+c
# value = calc(15,5,10)
# print(value)
# print(value+5)

# 여러 값 반환 / 언패킹
# - 쉼표로 여러 값을 return하면 튜플로 묶여서 들어옴 -> 언패킹 가능
# def min_max(values):
#     return min(values), max(values)

# print(min_max([75, 10, 100]))   #(10,100)
# low, high = min_max([75, 10, 100])
# print(low, high)

def report(a,b):
     print(a,b)
none = report("품질",10)
print(none)     # None -> reture 값이 없는 함수 호출하면 나오는 값

# 실습5 
def min_max(values):
    return min(values),max(values),sum(values)/len(values)
mini, maxi, mean = min_max([78, 85, 92])
print(mini,maxi,mean)
