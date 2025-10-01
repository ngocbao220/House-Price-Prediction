import numpy as np
import pandas as pd
from train import model
from loadData import house_data

def app():
    cols = house_data.columns
    data = []

    print("="*80)
    print('Predict House Price System')
    print('Sample input: 7420,4,2,3,yes,no,no,no,yes,2,yes,furnished \n yes - > type 1 \n no - > type 0 \n furnished - > type 2 (0,1,2)')
    print("="*80)

    data.append(input(f'Enter area:'))

    for col in cols[2:]:
        data.append(input(f'Enter {col} ({house_data[col].unique()}):'))
    
    predicted_price = model.predict(np.asarray(data, dtype=float).reshape(1, -1))[0]

    print(f"Predicted House price: {predicted_price:.2f}")
