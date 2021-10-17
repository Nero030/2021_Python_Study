''' <function_name>(<arguments>) '''

# 도움말
print(help(abs))
# 절댓값
print(abs(-9))
# 반올림
print(round(4.3))
print(round(3.141592653, 3)) # 세 번째 인수가 가르키는 자릿수 까지
# 제곱&나머지
print(pow(2, 4))
print(pow(2, 4, 3))
# 정수화
print(int(34.6))
# 실수화
print(float(21))

# 사용자 정의 함수
''' def <function_name>(<parameters>):
        <block>                       
        return <expression>           '''

def convert_to_celsius(fahrenheit) :
    return (fahrenheit -32) * 5 / 9

print(convert_to_celsius(80))

def quadratic(a, b, c, x) :
    first = a * x ** 2
    second = b * x
    third = c # first, second, third : 지역변수, a, b, c, x : 매개변수
    return first + second + third

print(quadratic(2, 3, 4, 1.5))
