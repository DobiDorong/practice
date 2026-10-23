# replace - 바꾸기/지우기
# 형식: 문자열.replace('바꿀 것', '새 것')
# - 모두 바꾸기, 결과 저장 필요

# print('정 상 가 동'.replace(' ',''))
# print('010-1234-5678'.replace('-',''))
# print('3,000'.replace(',',''))
# 체이닝 활용 가능 -> 여러 종류 문자 대체 차례대로 변경

# split - 구분자로 나누기 (결과 -> 리스트)
# 형식: 문자열.split('구분자')   구분자 생략 = 공백이 기준
# print('A1 A2 A3'.split())
# print('사과, 배, 감'.split(','))

# word = '설비 정상 가동'
# word = word.replace('정상','점검')
# print(word)

# title = 'PUMP A 03'
# title = title.split()
# print(title)

# code = 'a,b,c,d'
# code = code.split(',')
# print(code)


# code = 'a,b,c,d'
# code = code.split(',',2)
# print(code)

# join - 합치기 (리스트 -> 문자열)
# 형식: '구분자'.join(리스트) - 구분자가 앞에 온다
# print('-'.join(['2025', '01','15']))

# split + join
# - split: 문자열 -> 리스트
# - join: 리스트 -> 문자열
# raw = '사과, 배, 감'
# p = raw.split(',')
# print(p)        # ,를 기준으로 나누니까 공백도 들어감
# print('/'.join([p[0].strip(), p[1].strip(), p[2].strip()]))    # 공백 제거해서 합치기

# 실습5
# data = ['2025', '01', '15']
# print('-'.join(data))

# 실습6
# print('2025','1','15',sep='-',end='/')
# print('2025','1','15',sep=',')

# 실습7
# date = '2025/01/15'
# spl = date.split('/')
# jo = '-'.join(spl)
# print(jo)

# 실습8
label = '1,NORMAL ,25.5'
status = label.split(',')[1].strip().lower()
print(status)