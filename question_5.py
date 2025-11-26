import pandas as pd
mtcars = pd.read_csv('mtcars.csv')
cars_m_h = mtcars[['mpg', 'hp']].copy()
cars_m_h.columns = ['miles_per_gallon', 'horse_power']
cars_m_h.rename(columns={'miles_per_gallon': 'mpg', 'horse_power': 'hp'}, inplace=True)
print(cars_m_h)