#   [ 1. if ]

# (형태)
# if 조건:
#     실행 명령문

weather = input(" 오늘 날씨는 어때요? ")  # input : 사용자의 입력을 받음
  # 사용자가 입력을 하면 그 입력값은 문자열 형태로 weather에 저장됨
if weather == "비" or weather == "눈": # or 을 추가해서 조건을 추가할 수 있음
    print("우산을 챙기세요")  # 조건이 충족되지 않으면 아무것도 실행되지 않음
elif weather == "미세먼지":
    print("마스크를 챙기세요")
else:  # if도 elif도 아닐 경우 -> else
    print("준비물이 필요없어요")

temp = int(input("기온은 어때요?")) # 사용자가 입력한 입력값을 정수 형태로 받아서 temp에 저장
# input은 항상 문자열로 값을 받기 때문에 정수로 값을 받고 싶으면 int로 묶어줌
if 30 <= temp:
    print("너무 더워요. 나가지 마세요")
elif 10 <= temp and temp < 30:  # and  -> 앞 조건, 뒷 조건 둘다 성립할 경우
    print("괜찮은 날씨에요")
elif 0 <= temp < 10:  # and 없이 한번에 표현할 수도 있음 
    print("외투를 챙기세요")
else:
    print("너무 추워요. 나가지 마세요")



#   [ 2. for ]

# 여러번 반복해야 되는 작업을 for을 통해서 한번에 출력할 수가 있다.

for waiting_no in [0, 1, 2, 3, 4]:
    print("대기번호 : {0}".format(waiting_no)) # 차례대로 0 -> 4가 들어가서 실행 명령문을 수행
         # 여기서 {0} 은 format 괄호 안 0번 자리에 위치한 변수를 넣을 것이라는 것.

                # randrange() 와 비슷 
for waiting_no in range(5): # 0부터 5미만까지(0~4) 숫자를 차례대로 입력할 경우에는 이렇게 적어도 됨
    print("대기번호 : {0}".format(waiting_no))

for waiting_no in range(1,6): # 1부터 6 직전 수 까지(1~5)
    print("대기번호 : {0}".format(waiting_no))

starbucks = ["아이언맨", "토르", "아이엠 그루트"]
for customer in starbucks:
    print("{0}, 커피가 준비되었습니다.".format(customer))



#   [ 3. while ]

# (형태)
# while(조건):  # 조건이 만족할 때까지 명령실행문을 반복해라
#     명령실행문

# case 1) 스타벅스에서 손님을 5번 불렀는데도 안나오면 커피를 버리는 정책을 만들었다고 가정.

customer = "토르"
index = 5  # 5번을 확인하기 위한 장치
while index >= 1:                                              # 0번자리, 1번자리
    print("{0}, 커피가 준비 되었습니다. {1} 번 남았어요.".format(customer, index))
    index -= 1
    if index == 0:  # 즉, 5번 호출 한것.
        print("커피가 폐기처분되었습니다.")

# case 2) 다른 커피숍에서는 손님이 나올때까지 계속부름
customer = "아이언맨"
index = 1
while True:  # 무한루프를 돌게됨.  crtl + c  -> 강제종료
    print("{0}, 커피가 준비 되었습니다. 호출 {1} 회.".format(customer, index))
    index += 1

# case 3) 종업원이 손님을 부름
#         원하는 손님이 찾아오면 커피를 주고, 그렇지 않으면 계속해서 부름
 
customer = "토르"
person = "Unknown" # 종업원이 여쭤볼 손님의 이름

while person != customer: # 원하는 손님이 찾으러 오지 않음
    print("{0}, 커피가 준비 되었습니다.".format(customer))
    person = input("이름이 어떻게 되세요?  ")  
    # 원하는 손님이 아닐 경우, while문 계속해서 반복. 원하는 손님일 경우, while문 탈출
    if person == customer:
        print("{0}, 주문하신 커피 드릴게요.".format(customer))
        


#   [ 4. continue와 break ]

# 반복문 내에서 사용가능

# 출석번호에 따라서 아이들에게 책을 읽으라고 시킴
# 2번과 5번이 결석을함. 2번과 5번을 제외하고 나머지 아이들에게 읽으라고 시킴 -> continue
# 책을 안가져온 7번을 보고 화가나신 선생님이 수업을 마침.

absent = [2, 5]  # 결석을 함
no_book = [7] # 책을 안가져옴
for student in range(1,11): # student라는 변수를 선언. 1~10
    if student in absent:  # absent라는 리스트 안에 포함 됬는지 여부를 확인
        continue  # : 밑에 있는 문장을 실행하지 않고, 다음 반복으로 넘어감
    elif student in no_book:
        print("오늘 수업 여기까지. {0}번은 교무실로 따라와".format(student))
        break  # : 그 뒤에 반복값(8,9,10)이 있든 없든 상관없이 반복문을 탈출
    print("{0}번, 책을 읽어봐".format(student))

# continue : 그 자리에서 처음으로 돌아가서 계속해서 반복문을 진행
# break : 지금 상황에서 반복문을 종료하고 끝냄



#   [ 5. 한 줄 for ]

# 출석번호가 1 2 3 4, 앞에 100을 붙이기로 함 -> 101 102 103 104
students = [1,2,3,4,5]
print(students) # [1, 2, 3, 4, 5]

students = [i+100 for i in students]
# 리스트 students에 있는 값들(-> i)에 100을 각각 더해서 다시 리스트 students에 할당
print(students) # [101, 102, 103, 104, 105]

# 학생 이름을 길이로 변환
students = ["Iron man", "Thor", "I am groot"]
print(students)
students = [len(i) for i in students]
print(students)  # [8, 4, 10]

# 학생 이름을 모두 대문자로 바꿈
students = ["Iron man", "Thor", "I am groot"]
print(students)
students = [i.upper() for i in students]
print(students)  # ['IRON MAN', 'THOR', 'I AM GROOT']

# 학생 이름을 모두 소문자로 바꿈
students = [i.lower() for i in students]
print(students)  # ['iron man', 'thor', 'i am groot']



