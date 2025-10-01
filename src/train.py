from preprocessing import X_train, Y_train

from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

model = LinearRegression()

model.fit(X_train, Y_train)

training_pred = model.predict(X_train)

print(f'training MSE loss: {r2_score(y_pred=training_pred, y_true=Y_train)}')
