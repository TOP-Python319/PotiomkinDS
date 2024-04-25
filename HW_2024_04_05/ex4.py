import random

with open('random.txt', 'w', encoding='utf-8') as file:
    for _ in range(25):
        num = random.randint(111, 777)
        file.write(str(num) + '\n')

###############################################

# 461
# 384
# 148
# 314
# 433
# 722
# 173
# 593
# 375
# 437
# 416
# 368
# 492
# 209
# 468
# 429
# 678
# 667
# 163
# 272
# 687
# 417
# 452
# 659
# 205
