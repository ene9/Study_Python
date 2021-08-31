# Quiz) 당신은 Cocoa 서비스를 이용하는 택시 기사님입니다.
# 50명 승객과 매칭 기회가 있을 떄, 총 탑승 승객 수를 구하는 프로그램을 작성하시오.

# 조건1 : 승객별 운행 소요 시간은 5분 ~ 50분 사이의 난수로 정해집니다.
# 조건2 : 당신은 소요 시간 5분 ~ 15분 사이의 승객만 매칭해야 합니다.

# (출력문 예시)
# [0] 1번째 손님 (소요시간 : 15분)
# [ ] 2번째 손님 (소요시간 : 50분)
# [0] 3번째 손님 (소요시간 : 5분)
# ...
# [ ] 50번째 손님 (소요시간 : 16분)

# 총 탑승 승객 : 2 분



# (내가 쓴 답)

from random import *
customer = 0  # 총 탑승 승객

for chance in range(1,51):  # 50명과의 매칭기회
    time = randrange(5,51) # 5분에서 50분 사이의 난수
    if 5 <= time <= 15:
        print("[O] {0}번째 손님 (소요시간 : {1})".format(chance, time))
        customer += 1
    elif time < 5 or 15 < time:  # 굳이 elif로 조건을 쓰지 않아도, else로도 가능
        print("[ ] {0}번째 손님 (소요시간 : {1})".format(chance, time))
    
print("\n 총 탑승 승객 : {0} 분".format(customer))



# (강의 풀이)
from random import *
cnt = 0  # 총 탑승 승객
for i in range(1,51):  # 1 ~ 50이라는 수 (승객)
    time = randrange(5, 51)  # 5분 ~ 50분 소요 시간
    if 5 <= time <= 15:  # 5분 ~ 15분 이내의 손님(매칭 성공), 탑승 승객 수 증가 처리
        print("[O] {0}번째 손님 (소요시간 : {1})".format(i, time))
        cnt += 1
    else:  # 매칭 실패
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i, time))

print("총 탑승 승객 : {0}분".format(cnt))
