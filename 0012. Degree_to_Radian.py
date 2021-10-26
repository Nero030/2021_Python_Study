import math

def dtr(a) :
    ''' 라디안 = (각도 * 2 * pi) / 360 '''
    b = (a * 2 * math.pi) / 360
    return b

d = int(input('각도를 입력하시오(degree): '))
y = math.sin(dtr(d))
print('sin%d도 = %.2f' %(d, y))
