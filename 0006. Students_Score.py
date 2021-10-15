import statistics

pop = int(input('학생 인원수는? : '))
data = []

for i in range(pop) :
    data.append(int(input('점수를 입력하세요: ')))

print(end = '\n')

print('최고점은', max(data), '입니다.')
print('최저점은', min(data), '입니다.')
print('모든 점수의 합은', sum(data), '입니다.')
print('모든 점수의 평균은', statistics.mean(data), '입니다.')





