import numpy as np
import pandas as pd
%matplotlib inline
from matplotlib import pyplot as plt
import seaborn as sns
plt.style.use('ggplot')


df = pd.read_csv('yeezydb.csv')


df.columns.tolist()
df.shape
df['NAME'].value_counts()
df['SIZE'].value_counts()


df['RESELL_PRICE'] = df['RESELL_PRICE'].str.slice(start=1)
df['RETAIL_PRICE'] = df['RETAIL_PRICE'].str.slice(start=1)
df['RESELL_PRICE'] = df['RESELL_PRICE'].str.replace(',','')
df['RESELL_PRICE'] = pd.to_numeric(df['RESELL_PRICE'])
df['RETAIL_PRICE'] = pd.to_numeric(df['RETAIL_PRICE'])


plt.hist(df['SIZE'], bins=20)
plt.xlabel('Size')
plt.ylabel('323 Transactions')
plt.title('Histogram of Size', fontsize = 20)

plt.hist(df['RESELL_PRICE'])
plt.xlabel('Resell Price')
plt.ylabel('323 Transactions')
plt.title('Histogram of Transaction', fontsize = 20)

plt.scatter(df['SIZE'], df['RESELL_PRICE'])
plt.xlabel('Size')
plt.ylabel('Resell Price')

plt.figure(figsize=(12,6))
df.groupby('NAME')['ONEY_SALE'].median().sort_values(ascending=False).plot.bar(color='r')

df[['RETAIL_PRICE', 'RESELL_PRICE']].boxplot(by='RETAIL_PRICE', column = 'RESELL_PRICE')
plt.ylabel('Resell Price')
plt.xlabel('500             350V2     350V2(Glow)             700')

sns.kdeplot(df['RESELL_PRICE'], shade=True, label='Estimated PDF of Yeezy Boost Resell Price')

sns.jointplot(df['RESELL_PRICE'], df['SIZE'])