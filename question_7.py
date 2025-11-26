import pandas as pd
mtcars = pd.read_csv('mtcars.csv')
cars_m_h = mtcars[['mpg', 'hp']].copy()
cars_m_h_s = cars_m_h.iloc[9:35].reset_index(drop=True)
print(cars_m_h_s.drop_duplicates().reset_index(drop=True))