# 파이썬에서 제공하는 몇가지 숫자처리함수

print(abs(-5)) # -5에 대한 절댓값 = 5
print(pow(4,2)) # 4의 2승 = 16, pow(a, b) => a^b.
print(max(5, 12)) # 범위 (5 ~ 12)에서의 최댓값, 12
print(min(5, 12)) # 범위 (5 ~ 12)에서의 최솟값, 5
print(round(3.14)) # 3, 반올림
print(round(4.99)) # 5

from math import * # 'math library 안에 있는 모든 것을 이용하겠다'는 것.
print(floor(4.99)) # 내림 , 4
print(ceil(3.14)) # 올림, 4
print(sqrt(16)) # 제곱근, 4