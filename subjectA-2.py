'''

subjectA-2

'''

import random

print('サイコロ\n')

numbers = list(range(1, 7))


def dice():
    print(random.choice(numbers))


dice()
