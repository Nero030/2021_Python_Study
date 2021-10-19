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

''' 메모리 모델로 함수 호출 추적 ??
def f(x) :
    x = 2 * x
    return x # ??????????????

print(x = 1)
print(x = f(x + 1) + f(x + 2))'''

# 함수 작성시 :
# 함수명은 무엇으로 할것인가?
# 매개변수는 무엇이고 각 매개변수는 어떤 종류의 정보를 참조하는가?
# 그 정보로 어떤 계산을 수행하는가?
# 함수가 반환하는 정보는 무엇인가?
# 기대대로 작동하는가?

def days_difference(day1: int, day2: int) -> int : # 헤더, -> 타입표기 (생략가능)
    '''day1과 day2간 날짜수 차이를 반환한다.
    이때 day1과 day2는 1에서 365 사이의 값이다.''' # 설명
    return day2 - day1 # 본문

print(days_difference(200, 224)) # 테스트

# EX) 세개의 생일 계산 함수 디자인
# 일요일 1, 월요일 2, 화요일 3, 수요일 4, 목요일 5, 금요일 6, 토요일 7

def get_weekday(current_weekday: int, days_ahead: int) -> int :
    '''current_weekday에서 day_ahead만큼 지나면 무슨 요일인지 반환한다.
       current_weekday는 현재 요일로서 범위는 1부터 7까지이다.
       days_ahead는 오늘부터 며칠 후인지 뜻한다.'''
    return (current_weekday + days_ahead - 1) % 7 + 1

print(get_weekday(3, 1))
