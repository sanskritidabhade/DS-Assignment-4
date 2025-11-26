import pandas as pd
mtcars = pd.read_csv('mtcars.csv')
cars_m_h = mtcars[['mpg', 'hp']].copy()
cars_m_h.columns = ['miles_per_gallon', 'horse_power']
print(cars_m_h)