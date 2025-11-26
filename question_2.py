import pandas as pd
mtcars = pd.read_csv('mtcars.csv')
print(mtcars.drop('hp', axis=1))