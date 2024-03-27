from pathlib import Path
import pandas as pd
import random

pins = []
n = 50
for i in range(n):
    pin = ''
    for j in range(8):
        pin += str(random.randint(1, 9))
    pins.append(pin)

team_ids = list(range(1, n+1))

df = pd.DataFrame({'team': team_ids, 'pin': pins})
path = Path('../data/submission_pins.csv')

if not path.exists():
    df.to_csv(path, index=False)
