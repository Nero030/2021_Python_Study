def area_circumference(radius1, radius2) :
    area = radius1 * radius1 * 3.14
    circumference = radius2 * 2 * 3.14
    return area, circumference

text = int(input('원의 반지름 : '))

result1, result2 = area_circumference(text, text)

print('원의 면적은 {:.2f} 입니다.'.format(result1))
print('원의 둘레는 {:.2f} 입니다.'.format(result2))





