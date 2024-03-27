import generate_digit_coordinates
import random
import pandas as pd

number_coordinates = generate_digit_coordinates.gen_coordinates_from_digits([
                                                                            7, 3])

for i in range(len(number_coordinates)):
    number_coordinates[i][0] += random.random() * 0.1
    number_coordinates[i][1] += random.random() * 0.1

df_number = pd.DataFrame({
    'x': [x[0] for x in number_coordinates],
    'y': [x[1] for x in number_coordinates]
})

df_number['color'] = 'red'

random_coordinates = []
for i in range(10000):
    random_coordinates.append(
        [-3 + random.random() * 6, -3 + random.random() * 6])

df_random = pd.DataFrame({
    'x': [x[0] for x in random_coordinates],
    'y': [x[1] for x in random_coordinates]
})

df_random['color'] = 'blue'

df = pd.concat([df_number, df_random])
df = df.sample(frac=1)

print(df)

df.to_csv('../data/hidden_number.csv', index=False)
