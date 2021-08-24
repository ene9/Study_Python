# random 함수를 이용하여 난수를 뽑음

from random import *

print(random()) # 0.0 ~ 1.0 미만의 임의의 값을 생성

print(random() * 10) # 0.0 ~ 10.0 미만의 임의의 값을 생성

# 뒤의 소수들을 제외하고 정수값만 출력하고 싶을 떄 => int
print(int(random() * 10)) # 0 ~ 10이하의 임의의 정수값 생성 (int = 정수형 자료형)

print(int(random() * 10) + 1) # (0 <= x < 10) + 1 ==> (1 <= x < 11). 범위 +1

print(int(random() * 45) + 1 ) # 1 ~ 45 이하의 임의의 값 생성


print(randrange(1, 45)) # 1부터 45 미만의 임의의 값 생성. 마지막 수 포함x
print(randrange(1, 46)) # 1부터 46 미만(45이하). 마지막 수(46)는 포함하지 않음.

# 미만, 이하 헷갈릴때는
print(randint(1, 45)) # 1부터 45이하. 끝의 수들(1, 45) 모두 포함