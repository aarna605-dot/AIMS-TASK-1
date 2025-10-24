import pandas as pd
import numpy as np

data = {
    'ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Size': ['Small','Medium','Large','Medium','Small','Small','Large','Medium','Large','Medium'],
    'Price': [10, 20, 40, 50, 15, 25, 30, 20, 10, 30]
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

size_order = ['Small', 'Medium', 'Large']
ordinal_map = {category: index for index, category in enumerate(size_order)}

df['Size Encoded'] = df['Size'].map(ordinal_map)


print("DataFrame after Custom Ordinal Encoding:")
print(df)
print("\nOrdinal Map Used:")
print(ordinal_map)