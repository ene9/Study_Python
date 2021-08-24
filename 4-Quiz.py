Quiz) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오

예) http://naver.com
  규칙1 : http:// 부분은 제외 => naver.com
  규칙2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
  규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!"로 구성
              (nav)                  (5)             (1)           (!)
      예) 생성된 비밀번호 : nav51!
        
# [ 내가 쓴 답 ]
address = "http://naver.com"
address = address[7:]  # 규칙1 : http://는 어떤 주소든 7글자 이기때문에
address1 = address[:-4] # 규칙2 : 뒤에서부터 count하면 점(.)이 -4번째 이기 때문에  -> 이랬을때 주소가 .co.kr 인 경우에는 틀림
address2 = address1[0:3] # address2의 0번째부터 2번째까지

print(str(address2) + str(len(address)) + str(address.count("e")) + "!"  ) # 문자를 더해주는 것이기 때문에 정수값으로 출력되는 것들을 str로 묶어줌


# [ 강의 풀이 ]
url = "http://naver.com"
url2 = url.replace("http://", "") # 규칙1 : http:// 를 슬라이싱하기 보다는 공백으로 바꿔줌

url2 = url2[:url2.index(".")] # 규칙2 : url2.index(".") -> url2에서 점(.)있는 곳 직전까지 

password = url2[:3] + str(len(url2)) + str(url2.count("e")) + "!"  # 규칙3  : 문자끼리 더하는 것이기 때문에 정수값으로 출력되는 것들은 str로 묶어줌
print("{0}의 비밀번호는 {1}입니다.".format(url, password))
