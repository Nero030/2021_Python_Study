score = [73, 95, 80, 57, 99]

def func_sum(a) :
    total = a[0] + a[1] + a[2] + a[3] + a[4]
    return total

def func_aver(b) :
    mean = func_sum(b) / 5
    return mean


print('합계 점수 : ', func_sum(score))
print('평균 점수 : ', func_aver(score))

