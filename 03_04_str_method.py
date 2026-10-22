# 메서드 - 점(.) 문법
# 형식: 문자열.메서드이름() ---> 꼭 괄호를 붙여야 실행
# word = 'python'
# print(word.upper())
# print(word.count('p'))
# print(word)         # 원본값 그대로
# print('NORMAL'.lower())

# print('python is good'.capitalize())
# print('python nice'.title())

# word = 'ready'
# up = word.upper()
# print(up)

# word = 'WARNING'
# lo = word.lower()
# print(lo)

# word = 'kim chul soo'
# print(word.title())

# word1 = 'Fault'
# word2 = 'FAULT'
# print(word1 == word2)
# word1_1 = word1.lower()
# word2_1 = word2.lower()
# print(word1_1 == word2_1)

# 확인 메서드: is*** 메서드는 참/거짓 반환
# print('ABC'.isupper(),'abc'.islower())

# 공백 정리 - strip
# 형식: .strip() = 앞뒤 공백 제거
# raw = ' 정상 '
# print('['+raw+']')
# print('['+raw.strip()+']')

# .lstrip() -> 왼쪽 공백 제거 / .rstrip() -> 오른쪽 공백 제거
# 주의) strip은 '앞뒤' 공백만 제거, 가운데 공백 제거 X
# strip()으로 특정 문자 제거 -> strip('문자')
# s = '###정상###'
# print(s.strip('#'))

# a = 'ABC'
# b = 'abc'
# c = 'Abc'
# print(a.isupper(), a.islower())
# print(b.isupper(), b.islower())
# print(c.isupper(), c.islower())

# data = 'Sensor_LOG.CSV'
# data_lo = data.lower()
# print(data_lo.startswith('sensor'), data_lo.endswith('.csv'))

# word = ' 가동중 '
# print('['+word.strip()+']')

# word = ' 대기 '
# word_l = '['+word.lstrip()+']'
# word_r = '['+word.rstrip()+']'
# print(word_l+'/'+word_r)

# word = '***경고***'
# print(word.strip('*'))

# 체이닝 - 메서드 이어 붙이기
# 형식: 문자열.메서드1().메서드2() -> 왼쪽부터 차례로 메서드 적용
# clean = '   NORMAL   '.strip().lower()
# print(clean)

# notice = '   WARNING   '
# notice = notice.strip().lower()
# print(notice)

alarm = '  경보  '
alarm.strip()
print('['+alarm.strip()+']')
print('['+alarm+']')
alarm = alarm.strip()
print('['+alarm+']')