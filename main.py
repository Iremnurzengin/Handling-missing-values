#imputation and dropping

#importing librs
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#loading dataset 
dataset = pd.read_csv ('Placement_Dataset.csv')

print(dataset.head())
print(dataset.tail())
print(dataset.shape)
print(dataset.isnull().sum())

#tendencies : mean, median, mode 
#analiyse the distrubition of data in salary 
fig, ax = plt.subplot(figsize=(8,8))
sns.displot(dataset.salary)

#replace the missing value with median value 
dataset['salary'].fillna(dataset['salary'].median(),inplace=True)
dataset.isnull().sum()

#filling missing values with mean value or mode
#dataset['salary'].fillna(dataset['salary'].mean/mode(),inplace=True)

#Dropping method
salary_dataset = pd.read_csv('Placement_Dataset.csv')
print(salary_dataset.shape
print(salary_dataset.isnull())

#droping missing values
salary_dataset = salary_dataset.dropna(how='any')

#check number of missing values
salary_dataset.isnull().sum()

print(salary_dataset.shape)







