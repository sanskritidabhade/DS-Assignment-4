import pandas as pd
mtcars = pd.read_csv('mtcars.csv')
print(mtcars[['mpg', 'hp', 'vs', 'am', 'gear']])