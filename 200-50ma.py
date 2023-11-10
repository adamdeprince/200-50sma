import csv
import pandas as pd
import pandas_ta as ta
from fair_coin import f

CSV = pd.read_csv('SPX.csv')
X = pd.DataFrame(CSV['Close'])


X.ta.sma(50, append=True)
X.ta.sma(200, append=True)

death = None
flip_death = 0
flip_golden = 0
correct_death = 0
correct_golden = 0
up = 0
down = 0
try:
    for i, x in enumerate(X.loc):
        if None in (x.SMA_50, x.SMA_200):
            continue

        up += x.Close< X.loc[i+1].Close
        down += x.Close> X.loc[i+1].Close

        if death is None:
            death = x.SMA_50 < x.SMA_200 
        try:
            if death:
                if x.SMA_50 > x.SMA_200:
                    flip_golden += 1
                    correct_golden += X.loc[i+21*6].Close > x.Close
                    death = False
            else:
                if x.SMA_50 < x.SMA_200:
                    flip_death += 1
                    correct_death += X.loc[i+21*6].Close < x.Close
                    death = True
        except KeyError:
            break  # We're done
except KeyError:
    pass # X.loc doesn't terminate from a loop correctly. 
            
print("Up bias:", up / (up + down))

print("Predicted deaths:", flip_death)
print("Correct deaths:", correct_death)

print(up  / (up + down))
print(flip_death)
print(correct_death - flip_death)
print('Z: ', f(up / (up + down), correct_death, flip_death - correct_death))

print('Look for estiamtor of true probability https://en.wikipedia.org/wiki/Checking_whether_a_coin_is_fair')

print("Predicted golden:", flip_golden)
print("Correct golden:", correct_golden)
print('Z: ', f(up / (up + down), correct_golden, flip_golden - correct_golden))

