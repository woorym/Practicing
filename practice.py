import random
random.seed(50)

def first_rule():
    
    del ary[0]

def second_rule():

    point = ary.pop(0)
    ary.extend([point])

def third_rule():
    
    point = ary.pop()
    ary.insert(0,point)


# case1 = 0
# case2 = 0
sum = 0
# take = 0

ary = []
pos = []

size, count = map(int, input().split())

for i in range(size):
    ary.append(random.randint(0,10))

pos += map(int, input().split())

for j in range(len(pos)):
    take1 = 0
    take2 = 0
    case1 = 0
    case2 = 0
    change2 = 0
    for i in range(pos[j]-take1-1):

        second_rule()
        case1 += 1

    for i in range(len(ary)-pos[j]+1 + take2):

        third_rule()
        case2 +=1

    first_rule()

    change2 = len(ary) - case2


    if case1 <= case2:
        sum += case1
        if case1 ==0:
            continue
        take1 += case1 + 1
    else:
        sum += case2
        if case2 == 0:
            continue
        take2 += case2 - 3
    

print(sum)
    