import matplotlib.pyplot as plt
import seaborn as sns

from loadData import house_data

FIG_PATH = './fig'

# Show first 5 row
print(house_data.head())

# Show shape of Data
print(f"Shape of data: {house_data.shape}")

# Checking null data
print(f"Number of null data: {house_data.isnull().sum().sum()}")

# Show info of data
print(house_data.info())

# Show distribute of the columns
for col in house_data.columns:
    plt.figure(figsize=(10, 10))
    sns.histplot(house_data[col])
    plt.title(f'Distribute of {col}')
    plt.xlabel('Value')
    plt.ylabel('Count')
    plt.savefig(f'{FIG_PATH}/histplot_{col}')
    # plt.show()
