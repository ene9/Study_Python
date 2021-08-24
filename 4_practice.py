# [1. 문자열]

# 문자형 변수에 자료를 넣을때 작은따옴표(''), 큰 따옴표("") 모두 가능
sentence = '나는 소년입니다.'
print(sentence)
sentence2 = "파이썬은 쉬워요."
print(sentence2)

# 한줄이 아닌 여러줄에 걸쳐서 작성할 수도 있음
sentence3 = """
나는 소년이고,
파이썬은 쉬워요
"""
print(sentence3) # 큰 따옴표 넣은 부분도 포함하여 총 4줄 분량.



# [2. 슬라이싱]

# 슬라이싱 : 정보 중에서 필요한 만큼만 사용하는 것
jumin = "000906-4234567"  # 00(생년)09(월)06(일) 4(성별)23456(지역)7
#        012345678910111213 번째

print("성별 : " + jumin[7]) # jumin이라는 문자열 중에서 7번째 위치의 값을 가져옴
# 콜론(:)을 이용하여 범위 설정
print("생년 : " + jumin[0:2]) # 0번째부터 2번째 직전 값까지 즉, 0 ~ 1
print("월 : " + jumin[2:4]) # 2번째 부터 4번째 직전 값까지 즉, 2 ~ 3
print("일 : " + jumin[4:6]) # 4번째 부터 6번째 직전 값까지 즉, 4 ~ 5

print("생년월일 : " + jumin[:6]) # 처음부터 6번째 직전 값까지
print("뒤 7자리 : " + jumin[7:]) # 7번째부터 끝까지
print("뒤 7자리 (뒤에서부터) : " + jumin[-7:])
# 맨 뒤에서 7번째부터 끝까지.  4234567 여기서 맨 뒤의 수(7)가 -1번째, 맨 앞의 4는 -7번째.



# [3. 문자열처리함수]

python = "Python is Amazing"
print(python.lower()) # 모든 문자가 소문자로 바뀌어서 출력됨.
print(python.upper()) # 모든 문자가 대문자로 바뀌어서 출력됨.

# 0번째 문자가 대문자인지 확인
print(python[0].isupper()) # True
# 1번째 문자가 소문자인지 확인
print(python[1].islower()) # False

print(len(python)) # length 함수 : 문자열의 길이를 알려줌(띄어쓰기 포함, 띄어쓰기 또한 문자임.)

print(python.replace("Python", "Java")) # replace("a", "b") : 문자열 a -> b

index = python.index("n") # python이라는 변수에서 "n"이라는 문자가 몇 번째 위치해 있는지 알려줌
# 여기서는 start 위치가 처음(0번째 위치)부터.
print(index) # 5  5번째 위치에 n이 위치해 있음.
index = python.index("n", index + 1) # index + 1 이게 start 위치. -> 6(5+1)번째 위치 다음부터의 n의 위치
print(index) # 두번째 n의 위치

print(python.find("n")) # 5
print(python.find("is")) # 7 여기서 i가 7번째 위치에 있음.

# find와 index의 차이점 (찾고자 하는 문자가 없는 경우)
print(python.find("j")) # -1  찾고자 하는 문자가 없는 경우에는 -1로 반환 그리고 진행.
# print(python.index("J")) # index를 사용할 경우에는 찾고자 하는 문자가 없을때 오류를 내고 종료를 시켜버림
print("hi") # 위에서 오류 + 종료를 해버려서 이 코드도 실행이 안됨.

print(python.count("n")) # 2  n의 개수 count



# [4. 문자열 포맷]

print("a" + "b") # ab
print("a", "b") # a b
 # 이 방법 외에도 문자열을 출력하는 다양한 방법이 있음

#  방법 1
print("나는 %d살 입니다." % 20) # 퍼센트(%) 뒤에 있는 값을 이 문장 속의 %d위치에 넣겠다. (d -> 정수)

print("나는 %s을 좋아해요." % "파이썬")   # s(string) -> 문자열 

print("Apple이라는 단어는 %c로 시작해요." % "A") # c(charactor) -> 문자(한 글자)
# (C언어랑 헷갈리지 않기!) Python에서는 큰따옴표 뒤에 콤마 안찍어도됨.

# %s 로 쓰게 되면 정수건, 문자건 모두 쓸 수 있음
print("나는 %s살 입니다." % 20)
print("Apple은 %s로 시작합니다." % "A")
# 여러개
print("나는 %s색과 %s색을 좋아해요." % ("빨강", "파랑"))

# 방법 2
print("나는 {}살 입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요.".format("빨강", "파랑"))
# 나는 빨강색과 파랑색을 좋아해요.   순서대로 나옴
print("나는 {1}색과 {0}색을 좋아해요.".format("빨강", "파랑")) 
# 나는 파랑색과 빨강색을 좋아해요.
# "빨강"은 0번째 자리에, "파랑"은 1번째 자리에 위치.

# 방법 3
print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 20, color = "빨강"))
# 중괄호 안에 변수를 넣으면 format안에서 선언한 값을 그대로 사용가능
print("나는 {age}살이며, {color}색을 좋아해요.".format(color = "빨강", age = 20))
# 변수로 선언할 경우, 선언하는 순서 상관없어짐

# 방법 4 
age = 20
color = "파랑"
print(f"나는 {age}살이며, {color}색을 좋아해요.") 
# 중괄호 속의 변수는 실제 변수에서 사용되는 값을 그대로 갖다 씀.
age = 22
color = "노랑"
print(f"나는 {age}살이며, {color}색을 좋아해요.") 



# [5. 탈출문자]

# \n : 줄바꿈
print("백문이 불여일견\n백견이 불여일타") 

#  \"  \'  : 문장 내에서 따옴표로 출력됨
# 저는 "장은혜"입니다.    라고 출력하고 싶음.
# python에서는 "저는" 이렇게 끈 따옴표로 감싸주게 되면 한 문자열로 인식
print("저는 '장은혜'입니다.") # 이 방법도 있지만 ""로 묶고 싶음
print('저는"장은혜"입니다.') # 이제까지 문자열을 출력할때 항상 큰따옴표를 써왔음..

print("저는 \"장은혜\"입니다.")  # 역슬러쉬 + 큰따옴표(\")  :  문장 내에서 큰 따옴표로 출력하게 해줌
print("저는 \'장은혜\'입니다.")  # 역슬러쉬 + 작은따옴표(\')도 가능
 
# \\ : 문장 내에서 \(하나의 역슬러쉬)로 출력
# print(" C:\Users\장은혜\OneDrive\바탕 화면\PythonWorkPlace>") -> 오류
print(" C:\\Users\\장은혜\\OneDrive\\바탕 화면\\PythonWorkPlace>")
#  C:\Users\장은혜\OneDrive\바탕 화면\PythonWorkPlace>  이렇게 출력됨(역슬러쉬가 하나로)

#  \r  : 커서를 맨 앞으로 이동
print("Red Apple\rPine")
#  커서를 맨 앞으로 이동함으로써 "Red " 이 만큼을 Pine으로 채워짐

#  \b  : 백스페이스 ( 앞의 한 글자 삭제 ) 
print("Redd\bApple") # RedApple

#  \t  : 탭 (4칸 띄움)
print("Red\tApple") # Red    Apple (4칸 띄움)