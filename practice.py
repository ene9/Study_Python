print(1 != 3) # 등호 두개(==)는 같다. 느낌표와 등호(!=)는 같지 않다.
print(not(1 != 3)) # not : 뒤에 있는 값의 반대 

print((3 > 0) and (3 < 5) ) # True 두개 모두 true이어야함.  AND(&)연산
print((3 > 0) & (3 < 5)) # 위의 코드와 같음. 

print((3 > 0) or (3 > 5)) # True 둘 중 하나라도 true면 모두 true.  OR(|)연산
print((3 > 0) | (3 > 5)) # True
print((3 < 0) | (3 > 5)) # 두개 모두 false니까 결과도 따라서 False