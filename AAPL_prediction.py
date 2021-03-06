import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_csv('/content/AAPL.csv')

df.describe()

df.info()

df.head(5)

df['date'] = pd.to_datetime(df['date'])
df['year']= df['date'].dt.year
df['month']= df['date'].dt.month
df['day']= df['date'].dt.day

df=df.drop(columns=['date','symbol'])

df['divCash'].value_counts()

hassna=df.corr()

f, ax = plt.subplots(figsize=(10, 10))
mask = np.triu(np.ones_like(hassna, dtype=bool))
sns.heatmap(hassna,annot=True,ax=ax,linewidths=.5,cmap="YlGnBu",mask=mask);

from sklearn.preprocessing import MinMaxScaler
scaler=MinMaxScaler(feature_range=(0,1))
new_df=scaler.fit_transform(df)

print(type(new_df))

df_new = pd.DataFrame(new_df, columns = ['close', 'high', 'low', 'open', 'volume', 'adjClose', 'adjHigh','adjLow', 'adjOpen', 'adjVolume', 'divCash', 'splitFactor', 'year','month', 'day'])

df.columns.values

df_new

df_new.describe()

hasssna=df_new.corr()
f, ax = plt.subplots(figsize=(10, 10))
mask = np.triu(np.ones_like(hasssna, dtype=bool))
sns.heatmap(hasssna,annot=True,ax=ax,linewidths=.5,cmap="YlGnBu",mask=mask);

X=df_new.iloc[:,1:]
y=df_new['close']

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3)

from sklearn.linear_model import LinearRegression
reg = LinearRegression().fit(X, y)
print('the model score is:',reg.score(X,y)*100,'%')
