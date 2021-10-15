items = {"커피": 7, "펜": 3, "종이컵": 2, "우유": 1, "콜라": 4, "책": 5}
print('초기 재고', items)
print(end='\n')

while True:
    print('1.재고 수량 조회, 2.재고 수량 변경')
    print(end='\n')
    a = int(input("번호를 입력하세요 (0이면 종료.) : "))
    print(end='\n')

    if a == 1:
        b = str(input("물건의 이름을 입력하시오: "))
        print("재고 수량은 {}개".format(items[b]))
        print(end = '\n')

    elif a == 2:
        b = str(input("변경할 물건의 이름을 입력하시오: "))
        c = int(input("변경 수량을 입력하시오: "))
        print("{}의 수량은 {}개로 변경되었습니다.".format(b, c))
        items[b] = c
        print(end='\n')

    elif a== 0:
        break

    else:
        print("지원하지 않는 번호입니다.")
        print(end='\n')

