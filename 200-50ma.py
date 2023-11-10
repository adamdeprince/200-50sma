import csv
import pandas as pd
import pandas_ta as ta

CSV = pd.read_csv('SPX.csv')
X = pd.DataFrame(CSV['Close'])


X.ta.sma(50, append=True)
X.ta.sma(200, append=True)

death = None
flip_death = 0
flip_golden = 0
correct_death = 0
correct_golden = 0
try:
    for i, x in enumerate(X.loc):
        if None in (x.SMA_50, x.SMA_200):
            continue

        if death is None:
            death = x.SMA_50 < x.SMA_200 
        try:
            if death:
                if x.SMA_50 > x.SMA_200:
                    flip_golden += 1
                    correct_golden += X.loc[i+20].Close > x.Close
                    death = False
            else:
                if x.SMA_50 < x.SMA_200:
                    flip_death += 1
                    correct_death += X.loc[i+20].Close < x.Close
                    death = True
        except KeyError:
            break  # We're done
except KeyError:
    pass # X.loc doesn't terminate from a loop correctly. 
            
print("Predicted deaths:", flip_death)
print("Correct deaths:", correct_death)
print("Predicted golden:", flip_golden)
print("Correct golden:", correct_golden)


