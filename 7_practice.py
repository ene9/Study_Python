#   [ 1. 함수 ]

# (형태)
# def 함수이름():   -> 이렇게 함수를 정의.

def open_account():
    print("새로운 계좌가 생성되었습니다.")  
 # 함수는 정의만 해두는거지 실제로 호출을 하기 전까지는 실행되지 않음

open_account()  # 앞에서 정의해 두었던 함수를 호출



#   [ 2. 전달값과 반환값 ]
 
# 입금하는 함수 
def deposit(balance, money):  #  잔액, 입금할 금액
    print("입금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance + money))
    return balance + money  # 반환
    #  balance와 money 변수에 값을 입력하고 받은 그 값을 더하여 사용, 반환 
    # return을 통해서 (balance + money)값을 반환

balance = 0  # 처음 잔액
balance = deposit(balance, 1000)  # 1000원을 입금.  money -> 1000
# return을 통해 반환된 값을 balance에 저장.
print(balance)

# 출금하는 함수
def withdraw(balance, money):  # 잔액, 출금하려는 금액
    if balance >= money: # 잔액이 출금보다 많거나 같으면, 출금 가능
        print("출금이 완료되었습니다. 잔액은 {0}원 입니다.". format(balance - money))
        return balance - money
    else:  # 잔액이 출금보다 적을 경우
        print("출금이 완료되지 않았습니다. 잔액은 {0}원 입니다.".format(balance)) # 출금을 안했기때문에 잔액만
        return balance

# 앞에서 1000원을 입금했음
balance = withdraw(balance, 400)  # 400원을 출금하고자함
print(balance)

# 밤에 출금을 하고자함. 밤에는 수수료가 붙음
def withdraw_night(balance, money):  # 잔액, 출금하고자하는 금액
    commission = 100
    if balance >= (money + commission):  # 잔액보다 (출금하고자 하는 금액 + 수수료)가 작거나 같을 경우, 출금 가능
        print("출금이 완료되었습니다. 수수료는 {1}원이고, 잔액은 {0}원 입니다.".format(balance - (money + commission), commission))
        return commission, balance - (money + commission)  # 콤마를 이용해 두개의 값을 반환
    else:  
        print("출금이 완료되지 않았습니다. 잔액은 {0}원 입니다.".format(balance))
        return balance

# 앞에서 100원입금하고, 400원 출금했음
commission, balance = withdraw_night(balance, 200)



#   [ 3. 기본값 ]

def profile(name, age, main_lang):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}" \
        .format(name, age, main_lang))  # 이렇게 역슬러쉬(\)를 넣어줘야 줄바꿈 가능.
 
profile("유재석", 20, "파이썬")
profile("김태호", 25, "자바")

# 예를들어 나이와 주 사용 언어가 같은 경우, 반복적으로 같은 값을 적는 것은 비효율적임

# 기본값 사용
def profile(name, age=17, main_lang = "파이썬"):  # 나이와 주 사용언어가 각각 17, 파이썬으로 기본값이 설정됨
    print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}" \
        .format(name, age, main_lang)) 
    # 특정값을 전달받지 않았을 때에 할당된 기본값을 사용하겠다는 말.

profile("유재석")
profile("김태호", 18)  # age에 값을 따로 입력했을 경우에는 입력한 값이 출력됨



#   [ 4. 키워드값 ]

# 키워드값을 이용한 함수 호출
def profile(name, age, main_lang):
    print(name, age, main_lang)

# 함수에서 전달받는 매개 변수의 값을 키워드를 이용해서 함수를 호출. (이런식으로도 함수를 호출할 수 있다.)
profile(name = "유재석", main_lang = "파이썬", age = 20)
profile(main_lang = "자바", age = 25, name = "김태호")



#   [ 5. 가변인자 ]

# 가변인자를 활용한 함수 호출
def profile(name, age, lang1, lang2, lang3, lang4, lang5):
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end = " ")
    # end = " "  : end는 큰따옴표 띄어쓰기 큰따옴표 => 이걸 안썼다면 다음 print 명령문 출력이 줄바꿈이 된 뒤에 
    # 출력이 될텐데, 이걸 적음으로써 띄어쓰기를 한 다음 그 뒤로 다음 print 명령문 출력이 이러짐.
    print(lang1, lang2, lang3, lang4, lang5)
    # 두 문장이 하나의 문장으로 출력이 됨.

print("유재석", 20, "Python", "Java", "C", "C++", "C#")
print("김태호", 25, "Kotlin", "Swift", " ", " ", " ")

# 만약 유재석의 프로필에 언어를 더 추가하거나, 김태호의 프로필에 언어를 2개만 적고 싶은 경우 => 가변인자

def profile(name, age, *language):  # *langaue -> 원하는 대로 값을 넣을 수 있음
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end = " ")
    for lang in language:
        print(lang, end = " ")
    print()

print("유재석", 20, "Python", "Java", "C", "C++", "C#", "JavaScript")
print("김태호", 25, "Kotlin", "Swift")

# 서로 다른 개수의 값을 넣어줄때는 가변인자(즉, 별(*)로 시작되는 매개변수)를 활용할 수 있음



#   [ 6. 지역변수와 전역변수]

# 지역변수 : 함수 내에서만 쓸 수 있는 것. 함수가 호출될 때 만들어졌다가 함수 호출이 끝나면 사라짐
# 전역변수 : 프로그램 내에서 어디서든 부를 수 있는 변수

gun = 10

def checkpoint(soldiers):  # 경계근무(총 가지고 가는 군인 수)
    gun = 20
    gun = gun - soldiers  # 이 gun은 위에서 정의된 gun이 아니라 chechpoint함수 내에서 만들어진 변수
                          # 이게 바로 지역변수 !
    print("[함수 내] 남은 총 : {0}".format(gun))

print("전체 총 : {0}".format(gun))
checkpoint(2)
print("남은 총 : {0}",format(gun))

# 전체 총 : 10              checkpotin 함수 밖에서 만들어진 gun이라는 변수를 사용
# [함수 내] 남은 총 : 18     함수 내에서 만들어진 gun(=20)이라는 변수로 사용됨
# 남은 총 : {0} 10      

gun = 10

def checkpoint(soldiers):
    global gun  # 전역 공간(checkpoint 함수 밖)에 있는 gun을 사용
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))

print("전체 총 : {0}".format(gun))
checkpoint(3)
print("남은 총 : {0}".format(gun))

# 전체 총 : 10
# [함수 내] 남은 총 : 7 
# 남은 총 : 7

# 함수의 전달값(parameter)을 던져서 계산을 하고 반환값을 받아서 사용하는 방법

gun = 10

def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers   # 함수를 호출할 때 받은 gun(=10)과 soldier값(2)을 이용해 계산을 하고
    print("[함수 내] 남은 총 : {0}".format(gun))  # 계산된 값을 출력하고
    return gun   # 이 gun은 함수 내의 gun.  -> 반환해줌

print("전체 총 : {0}".format(gun))
gun = checkpoint_ret(gun, 2)  # 여기 괄호에 있는 gun은 밖에서 정의된 gun(=10).  
#  함수 내에서 계산된 값을 반환받은 바깥 gun.
print("남은 총 : {0}".format(gun))

