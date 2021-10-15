text1 = int(input ('첫번째 정수를 입력하세요. : '))
text2 = int(input ('두번째 정수를 입력하세요. : '))
text3 = int(input ('세번째 정수를 입력하세요. : '))

texts = [text1, text2, text3]

print(str(text1)+','+str(text2)+','+str(text3)+'중 가장 큰수는', str(max(texts))+'이다.')

# 문자열의 크기랑, 정수의 크기는 다른거다.
# ,와 +의 연결방식은 다르다. 문자열 + 문자열
# 형식 지정자 : print("%s, %s, %s 중 가장 큰 수는 %s입니다." %(text1, text2, text3, max(texts)))
