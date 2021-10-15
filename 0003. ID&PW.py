while 1:
    textID = input('아이디를 입력해주세요. : ')
    if textID == 'lovepython!':
        textPW = input('비밀번호를 입력해주세요. : ')
        if textPW == 'p12345':
            print('lovePython!님 환영합니다~!!')
            break
        elif textPW != 'p12345' :
            print('비밀번호가 틀립니다.')
    elif textID != 'lovepython!':
        print('아이디를 찾을수 없습니다.')


# 어떻게 하면 간단하게 아이디 틀리자마자 아이디 틀렸다고 나오게 할 수 있을까. -> 아이디 먼저 검사받고 패스워드
# -> 중첩 if문 사용


