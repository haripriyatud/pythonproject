import pandas as pd

df = pd.read_csv('employee_data.csv')

print(df.head())

print(df.tail())

print(df.columns)

print(df.dtypes)

print(df.describe())

print(df.index)

# sorting values in pandas dataframe - Sort by salary ascending order
print(df.sort_values(by="Salary",ascending=False))

# sorting values in pandas dataframe - Sort by salary descending order
print(df.sort_values(by="Salary",ascending=False))

# selecting multiple column in pandas data frame
print(df[['Name','Department']])

# filtering rows with Department 'HR'
HR_dataframe= df['Department']=='HR'

print(df[HR_dataframe])

# GroupBy example in Pandas dataframe: 

print(df.groupby(['Department'])['Salary'].mean())

print(df.groupby(['Department'])['Salary'].max())


