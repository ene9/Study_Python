#   [ 1. 리스트 ]

# 리스트 : 순서를 가진 객체의 집합
subway = [10, 20, 30]
print(subway)

subway = ["강아지", "토끼", "고양이"]
#          0번째    1번째     2번째
print(subway)

# 토끼가 몇 번째 칸에 탔는지?
print(subway.index("토끼"))  # 1

# 코끼리가 다음 정류장에서 다음 칸에 탐
subway.append("코끼리")
print(subway) # append : 맨 뒤에 붙도록 돼있음

# 여우를 강아지와 토끼 사이에 태워봄
subway.insert(1, "여우")  # 1번 자리에 여우를 넣음
print(subway)

# 지하철에 있는 사람을 한 명씩 뒤에서부터 꺼냄
print(subway.pop())  # 뒤에서부터 한명씩 꺼냄
print(subway)

# 같은 이름의 사람이 몇명 있는지 확인
subway.append("강아지")
print(subway)
print(subway.count("강아지")) # 2

# 정렬도 가능
num_list = [5,2,4,3,1]
num_list.sort()  # 정렬
print(num_list)  # [1,2,3,4,5]

# 순서 뒤집기 가능
num_list.reverse()
print(num_list)  # [5,4,3,2,1]

# 모두 지우기
num_list.clear()
print(num_list)  # []

# 다양한 자료형과 함께 사용
num_list = [5,2,4,3,1]
mix_list = ["토끼", 20, True] # 문자열, 정수, 불리안 모두 섞어서 사용 가능
print(mix_list)

# 리스트 확장
num_list.extend(mix_list)  # num_list에 mix_list값을 넣어서 확장함.
print(num_list)



#   [ 2. 사전 ]
# 사전에서 단어를 찾으면 그 단어와 그 단어에 대한 정의가 나옴
# 키에 대한 중복이 허용되지 않음
# key 하나 당 value가 주어짐
cabinet = {3 : "강아지", 100 : "토끼"} # 3이라는 key의 value는 강아지
print(cabinet[3]) # 강아지   key를 넣으면 해당 value가 출력됨
print(cabinet[100]) # 토끼

print(cabinet.get(3)) # 값을 가져오는 방법2. 이때는 소괄호!

# cabinet.get() vs cabinet[]  (찾으려는 key가 없을 때)
print(cabinet.get(5)) # 찾으려고 하는 key가 없음 -> none 출력 & 뒤의 코드 계속 진행
# print(cabinet[5]) # 찾으려고 하는 key가 없음 -> 오류 & 종료시킴
print("hi") # 위의 코드로 인해 출력이 안됨

print(cabinet.get(5, "avilable")) # available    5라는 없는 값을 가져올때 none말고 기본값을 쓰고 싶을때.
# 5라는 값을 가져오려고 시도를 할텐데, 없으면 available을 출력

# cabinet에 어떠한 key가 있나없나 확인
print( 3 in cabinet) # True
print( 5 in cabinet) # False

# key를 꼭 정수형으로 할 필요는 없음. 정수, 문자, 문자열 다 됨.
cabinet = {"A-3" : "강아지", "B-100" : "토끼", "룰루" : "랄라"}
print(cabinet["룰루"]) # 랄라
print(cabinet.get("B-100")) # 토끼

# key (& 그에 따른 value) 추가
print(cabinet)
cabinet["C-20"] = "코끼리" # C-20이라는 key에 코끼리라는 value를 넣음
cabinet["A-3"] = "귀여운 강아지" # 중복된 key name이라면 value가 update가 됨.
print(cabinet)

# key 제거
del cabinet["A-3"]  # del을 이용해서 특정 key 제거
print(cabinet) 

# key들만 출력
print(cabinet.keys()) 

# value들만 출력
print(cabinet.values())

# key, value 쌍으로 출력
print(cabinet.items())

# 모든 값을 제거 
cabinet.clear()
print(cabinet)  # {}



#   [ 3. 튜플 ]
# 튜플은 리스트와는 다르게 내용 변경이나 추가를 할 수 없음
# 리스트보다는 할게 많지 않은데, 속도가 빠름
# 리스트 : 변경되는 목록,  튜플 : 변경되지 않는 목록

menu = ("돈까스", "치즈까스")  # 튜플을 이용할때는 소괄호 안에서 콤마로 구분.
print(menu[0])  # 돈까스
print(menu[1])  # 치즈까스

# menu.add("생선까스")  -> 오류.  튜플은 내용을 변경할 수 없음

# 소괄호로 여러개의 변수를 선언
(name, age, hobby) = ("으네", 22, "코딩")   
print(name, age, hobby)