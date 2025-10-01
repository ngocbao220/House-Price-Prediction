from train import model
from preprocessing import X_test, Y_test
from sklearn.metrics import r2_score, root_mean_squared_error, mean_absolute_error

test_pred = model.predict(X_test)

print(f'test R2 score loss: {r2_score(y_pred=test_pred, y_true=Y_test)}')
print(f'test RMSE score loss: {root_mean_squared_error(y_pred=test_pred, y_true=Y_test)}')
print(f'test MAE score loss: {mean_absolute_error(y_pred=test_pred, y_true=Y_test)}')
