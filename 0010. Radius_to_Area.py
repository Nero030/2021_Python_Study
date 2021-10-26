def radius_to_area(radius) :
    area = radius * radius * 3.14
    return area

text = int(input('원의 반지름 : '))
print(radius_to_area(text))
