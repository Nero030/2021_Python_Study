class Circle :
    pi = 3.14
    def circleA(self, radius) :
        return self.pi * radius * radius
    def circleC(self, radius) :
        return 2 * self.pi * radius

c1 = Circle( )

text = int(input('반지름을 입력하세요 : '))

print('원의 면적: ', c1.circleA(text))
print('원의 둘레: ', c1.circleC(text))