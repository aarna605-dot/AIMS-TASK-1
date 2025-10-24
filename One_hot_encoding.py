import pandas as pd
import numpy as np

data = {
    'Product': ['A', 'B', 'C', 'A', 'D', 'C','A','D','B','A'],
    'Color': ['Red', 'Blue', 'Red', 'Orange', 'Blue', 'Green','Blue', 'Green', 'Blue', 'Orange'],
    'Value': [100, 200, 150, 120, 250, 180, 200, 220, 180, 100]
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

unique_colors = set()
for color in df['Color']:
    unique_colors.add(color)

unique_colors = sorted(list(unique_colors)) 

print(f"Unique Categories found: {unique_colors}")

for color_category in unique_colors:
    new_col_name = f'Color_{color_category}'

    df[new_col_name] = np.where(
        df['Color'] == color_category,
        1, 
        0  
    )

print("\n DataFrame after Custom One-Hot Encoding:")
print(df)

one_hot_cols = [col for col in df.columns if col.startswith('Color_')]
print(f"\nNew One-Hot Columns: {one_hot_cols}")
