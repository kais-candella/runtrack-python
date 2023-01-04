import operator
import random

operators = [('+', operator.add), ('-', operator.sub), ('*', operator.mul,)]

for i in range(1):
    num1 = float(input("Entrée un nombre: "))
    num2 = float(input("Entrée un nombre: "))
    op, fn = random.choice(operators)
    print("{} {} {} = {}".format(num1, op, num2, fn(num1, num2)))


# pour avoir les chiffres et les operateurs random

#import operator
#import random

#operators = [('+', operator.add), ('-', operator.sub), ('*', operator.mul,)]

#for i in range(10):
    #a = random.randint(1, 50)
    #b = random.randint(1, 50)
    #op, fn = random.choice(operators)
    #print("{} {} {} = {}".format(a, op, b, fn(a, b)))

