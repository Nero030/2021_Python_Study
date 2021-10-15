import random

print('산수 문제를 맞춰보세요~ (0이면 종료)')
while True:
    a = random.randint(1, 100)
    b = random.randint(1, 100)

    print(a, '+', b, '= ?')

    text = int(input('정답 : '))

    if text == a + b :
        print('참 잘했어요~')

    elif text == 0 :
        break

    else :
        print('공부 좀 더해!')


