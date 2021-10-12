# 4자리 정수의 각 자리 수의 합

while True:
    text = input('시작하시려면 아무키 입력. (종료하려면 quit 입력.) : ' )
    if text == "quit" :
        print('프로그램을 종료합니다.')
        break
    else :
        number = int(input('4자리 정수를 입력해주세요. : ' ))
        if 1000 <= int(number) <= 9999:
            print('각 자릿수의 합 : ' + str((number // 1000 + (number % 1000 - number % 100) // 100
                                       + (number % 100 - number % 10) // 10 + number % 10)))
        else :
            print('4자리 정수만 입력해주세요. (종료하려면 quit 입력.)')


# 이게 원하는대로 깔끔하게 잘 만들어지지가 않네요 ㅜㅜ..





























