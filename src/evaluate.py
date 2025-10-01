from train import model
from preprocessing import X_test, Y_test
from sklearn.metrics import r2_score

test_pred = model.predict(X_test)

print(f'test MSE loss: {r2_score(y_pred=test_pred, y_true=Y_test)}')
