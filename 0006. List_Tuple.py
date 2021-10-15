name = []
score = []


print('이름과 점수를 입력하세요 ("Enter"를 치면 입력을 종료합니다.)')

while True :
    n = (input('이름을 입력하시오 : '))
    name.append(n)

    n = (input('점수를 입력하시오 : '))
    score.append(n)

    if n == '' :
        info = dict(zip(name, score))
        info.popitem()
        print(info)
        break


