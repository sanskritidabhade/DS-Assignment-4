import pandas as pd
import re

with open('sales.txt', 'r', encoding='utf-8') as f:
    lines = [line.strip() for line in f if line.strip() and line.strip() != 'sales']

df = pd.DataFrame({'raw': lines})

def clean_amount(text):
    text = text.replace('£', '').replace('$', '')
    text = text.replace(',', '.')
    text = re.sub(r'[^\d.]', '', text)
    return pd.to_numeric(text, errors='coerce')

df['amount_original'] = df['raw'].apply(clean_amount)
df = df.dropna(subset=['amount_original']).reset_index(drop=True)

GBP_TO_USD = 1.27
df['currency'] = df['raw'].apply(lambda x: 'GBP' if '£' in x else 'USD')
df['sales_usd'] = df.apply(
    lambda row: round(row['amount_original'] * GBP_TO_USD, 2)
    if row['currency'] == 'GBP' else round(row['amount_original'], 2), axis=1)

tidy_sales = df[['sales_usd']].copy()
print(tidy_sales.head(20))
print(tidy_sales.describe())
tidy_sales.to_csv('sales_tidy_usd.csv', index=False)