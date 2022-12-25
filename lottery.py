import random

COUNTS = 100

reds = [i for i in range(1,34)]
blues = [j for j in range(1,17)]
# print(reds, blues)
print("start........")
for k in range(COUNTS):
    # random.seed()
    random.shuffle(reds)
    random.shuffle(blues)
    res_reds = reds[:6]
    res_reds.sort()
    res_blues = blues[:1]
    print(k+1, res_reds, res_blues)
    # if res_reds == [7,12,15,24,26,29] and res_blues == [6]:
    #     print(k, res_reds, res_blues)    
print("end..........")