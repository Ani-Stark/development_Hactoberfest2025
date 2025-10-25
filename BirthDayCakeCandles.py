import math
import os
import random
import re
import sys

# Complete the birthdayCakeCandles function below.
def birthCakeCandles(gr):
    count=0
    big = max(gr)
    for i in range(len(gr)):
        if(gr[i]==big):
            count+=1
    return count
        

if __name__ == '__main__':
    pftr = open(os.environ['OUTPUT_PATH'], 'w')

    gr_count = int(input())

    gr = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(gr)

    pftr.write(str(result) + '\n')

    pftr.close()
