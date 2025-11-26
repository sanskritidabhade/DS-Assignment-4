import pandas as pd
mtcars = pd.read_csv('mtcars.csv')
mtcars = mtcars.set_index('model')
print(mtcars.loc['Lotus Europa'])