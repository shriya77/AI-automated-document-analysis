import pandas as pd

from google.colab import files
uploaded = files.upload()
df = pd.read_csv("bank_loan.csv")

print("head\n\n", df.head())
print("info\n\n", df.info())
print("describe\n\n", df.describe())
print("columns\n\n", df.columns)
print("data types\n\n", df.dtypes)
print("null vals\n\n", df.isnull().sum())

df['CCAvg'] = df['CCAvg'].str.replace('/', '.', regex=False)
df['CCAvg'] = df['CCAvg'].astype(float)
df['Income'] = df['Income'] * 1000

df = df[
    (df['Experience'] >= 0) &
    (df['Income'] >= 0) &
    (df['Mortgage'] >= 0) &
    (df['CCAvg'] >= 0) &
    (df['Age'] >= 0) &
    (df['Family'] >= 0) &
    (df['Education'] >= 1)
]

df = df.drop(['ID', 'ZIP Code'], axis=1)

df['Personal Loan'] = df['Personal Loan'].map({0 : 'No', 1 : 'Yes'})
df['Securities Account'] = df['Securities Account'].map({0 : 'No', 1 : 'Yes'})
df['CD Account'] = df['CD Account'].map({0 : 'No', 1 : 'Yes'})
df['Online'] = df['Online'].map({0 : 'No', 1 : 'Yes'})
df['CreditCard'] = df['CreditCard'].map({0 : 'No', 1 : 'Yes'})

df.to_csv('bank_loan_cleaned.csv', index = False)
