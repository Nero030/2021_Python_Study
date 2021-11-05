import random

class XP :
    x = random.randint(1, 100)
    y = random.randint(1, 100)
    t = print(x, '+', y, '= ?')
    def random_problem(self, a, b) :
       p1 = a.x
       p2 = b.y
       return p1 + p2

p3 = XP()

print(p3.t)



