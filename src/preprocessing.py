import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

from loadData import house_data
from exploreData import FIG_PATH

# Convert classific type to numberic type

# airconditioning
print("After convert ")
house_data['airconditioning'] = house_data['airconditioning'].map({'yes': 1, 'no': 0})
print('airconditioning', house_data['airconditioning'].unique())

# basement
house_data['basement'] = house_data['basement'].map({'yes': 1, 'no': 0})
print('basement',house_data['basement'].unique())

# guestroom
house_data['guestroom'] = house_data['guestroom'].map({'yes': 1, 'no': 0})
print('guestroom', house_data['guestroom'].unique())

# hotwaterheating
house_data['hotwaterheating'] = house_data['hotwaterheating'].map({'yes': 1, 'no': 0})
print('hotwaterheating', house_data['hotwaterheating'].unique())

# mainroad
house_data['mainroad'] = house_data['mainroad'].map({'yes': 1, 'no': 0})
print('mainroad', house_data['mainroad'].unique())

# prefarea
house_data['prefarea'] = house_data['prefarea'].map({'yes': 1, 'no': 0})
print('prefarea', house_data['prefarea'].unique())

# furnishingstatus
house_data['furnishingstatus'] = house_data['furnishingstatus'].map({'furnished': 2, 'semi-furnished': 1, 'unfurnished': 0})
print('furnishingstatus', house_data['furnishingstatus'].unique())

# Show correlate of features
corr = house_data.corr()

sns.heatmap(corr, annot=True, cbar=True, cmap='Blues')
plt.title("Correlation of features")
plt.savefig(f'{FIG_PATH}/correlation')

# Split to X and Y
X = house_data.drop('price', axis=1)
Y = house_data['price']

# Standarized data
scaler = StandardScaler()

X = scaler.fit_transform(X)

print('X after standarizaion: ', X.std())

# Train test split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

print(f"X shape: {X.shape}, X_train shape: {X_train.shape}, X_test shape: {X_test.shape}")