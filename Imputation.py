import pandas as pd
import numpy as np

data = {
    'Age': [25, 30, np.nan, 45, 22, np.nan, 38],
    'City': ['NY', 'LA', 'NY', np.nan, 'SF', 'LA', 'SF'],
    'Score': [85, 92, 78, 95, 88, 70, 99]
}
df = pd.DataFrame(data)
print("Original DataFrame")
print(df)
print("\n Missing Value Counts: ")
print(df.isnull().sum())

age_sum = 0
age_count = 0
for age in df['Age']:
    
    if not pd.isnull(age):
        age_sum += age
        age_count += 1

mean_age = age_sum / age_count
print("Calculated Mean Age: {mean_age:}")

df['Age_Imputed'] = df['Age'] 

df['Age_Imputed'] = np.where(
    df['Age_Imputed'].isnull(),
    mean_age,
    df['Age_Imputed']
)

city_counts = {}
for city in df['City']:
    if not pd.isnull(city):
        city_counts[city] = city_counts.get(city, 0) + 1

mode_city = None
max_count = -1
for city, count in city_counts.items():
    if count > max_count:
        max_count = count
        mode_city = city

print("Calculated Mode City: {mode_city}")

df['City_Imputed'] = df['City'] 

df['City_Imputed'] = np.where(
    df['City_Imputed'].isnull(),
    mode_city,
    df['City_Imputed']
)

print("\n DataFrame after Imputation:")
print(df[['Age', 'Age_Imputed', 'City', 'City_Imputed']])
