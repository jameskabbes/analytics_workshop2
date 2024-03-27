import pandas as pd
import numpy as np

import datetime

# Define the start and end dates for the time series

current_datetime = datetime.datetime(2023, 1, 1, 0, 0, 0)
end_datetime = datetime.datetime(2024, 1, 1, 0, 0, 0)

datetimes = []
while current_datetime < end_datetime:
    datetimes.append(current_datetime)
    current_datetime += datetime.timedelta(hours=1)

df = pd.DataFrame(
    {'datetime': [datetime.datetime.isoformat(dt) for dt in datetimes], })
df['value'] = np.random.random(size=len(df))

df.to_csv('../data/time_series.csv', index=False)
