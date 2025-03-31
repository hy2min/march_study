# 메서드는 클래스 내부에 정의되는 함수
# 클래스는 파이썬에서 '타입을 표현하는 방법'이며 이미 은연중에 사용해왔음
# 문자열 메서드
# s.find(x) : x의 첫 번째 위치를 반환. 없으면 -1을 반환
# s.index(x) : x의 첫 번째 위치를 반환. 없으면 오류 발생
# s.isupper() : 문자열 내의 모든 문자가 대문자인지 확인
# s.islower() : 문자열 내의 모든 문자가 소문자인지 확인
# s.isalpha() : 문자열 내의 모든 문자가 알파벳인지 확인
# s.replace(old, new[,count]) : 바꿀 대상 글자를 새로운 글자로 바꿔서 반환
# s.strip() : 공백이나 특정 문자를 제거
# s.split() : sep를 구분자 문자열로 사용하여 문자열에 있는 단어들의 리스트를 반환
# 'seperator'.join(iterable) : 구분자로 iterable의 문자열을 연결한 문자열을 반환
# s.capitalize() : 가장 첫 번째 글자를 대문자로 변경
# s.title() : 문자열 내 띄어쓰기 기준으로 각 단어의 첫 글자는 대문자로, 나머지는 소문자로 변환
# s.upper(), s.lower(), s.swapcase()

# 리스트 메서드
# L.append(x) : 리스트 마지막에 항목 x를 추가
# L.extend(m) : iterable m의 모든 항목들을 리스트 끝에 추가
# L.insert(i,x) : 리스트 인덱스 i에 항목 x를 삽입
# L.remove(x) : 리스트 가장 왼쪽에 있는 첫번째 x를 제거, 항목이 존재하지 않을 경우 ValueError
# L.pop() : 리스트 가장 오른쪽에 있는 항목(마지막)을 반환 후 제거
# L.pop(i) : 리스트의 인덱스 i에 있는 항목을 반환 후 제거
# L.clear() : 리스트의 모든 항목 삭제
# L.index(x) : 리스트에서 첫 번째로 일치하는 항목 x의 인덱스를 반환
# L.count(x) : 리스트에서 항목 x의 개수를 반환
# L.reverse() : 리스트의 순서를 역순으로 변경
# L.sort() : 리스트를 정렬 (매개변수 이용가능)

# 얕은 복사 : 객체의 최상위 요소만 새로운 메모리에 복사하는 방법
# 내부에 중첩된 객체가 있다면 그 객체의 참조만 복사됨
# 구현방법 : 1. 리스트 슬라이싱, 2. copy() 메서드, 3. list() 함수

# 깊은 복사 : 객체의 모든 수준의 요소를 새로운 메모리에 복사하는 방법
# 중첩된 객체까지 모두 새로운 객체로 생성됨
# import copy
# new_object = copy.deepcopy(original_object)

# isdecimal() : 문자열이 모두 숫자 문자 (0~9)로만 이루어져 있어야 True
# isdigit() : 유니코드 숫자도 인식
# isnumeric() : 추가적인 유니코드 문자들을 인식

# 딕셔너리 메서드
# D.clear() : 딕셔너리의 모든 키/값 쌍을 제거
# D.get(k) : 키 k에 연결된 값을 반환 (키가 없으면 None을 반환)
# D.get(k, v) : 키 k에 연결된 값을 반환하거나 키가 없으면 기본 값으로 v를 반환
# D.keys() : 딕셔너리의 키를 모은 객체를 반환
# D.values() : 딕셔너리의 값을 모은 객체를 반환
# D.items() : 딕셔너리의 키/값 쌍을 모은 객체를 반환
# D.pop(k) : 딕셔너리 D에서 키 k를 제거하고 연결됐던 값을 반환
# D.pop(k,v) : 딕셔너리 D에서 키 k를 제거하고 연결됐던 값을 반환 (없으면 v를 반환)

# 집합 메서드
# s.add(x) : 세트 s에 항목 x를 추가. 이미 x가 있다면 변화 없음
# s.clear() : 세트 s의 모든 항목을 제거
# s.remove(x) : 세트 s에서 항목 x를 제거. 항목 x가 없을 경우 Key error
# set1.difference(set2) : 차집합 (set1 - set2)
# set1.intersection(set2) : 교집합 (set1 & set2)
# set1.issubset(set2) : set1이 부분집합이면 True 반환
# set2.issubset(set1) : set2가 부분집합이면 True 반환
# set1.union(set2) : 합집합 (set1 | set2)