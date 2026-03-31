import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

train = pd.read_csv("./data/regression_exercise_training_data.csv")
test = pd.read_csv("./data/regression_exercise_test_data.csv")

X_train = train[['X_train']].values
y_train = train['y_train'].values

X_test = test[['X_test']].values
y_test = test['y_test'].values

print("\n\nDecisionTreeRegressor Results:")
for depth in [1, 3, 5, None]:
    dt = DecisionTreeRegressor(max_depth=depth, random_state=42)
    dt.fit(X_train, y_train)
    y_pred = dt.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    print(f"max_depth={depth}, MSE={mse:.4f}")

print("\n\nRandomForestRegressor Results:")
for n in [1, 20, 100]:
    rf = RandomForestRegressor(n_estimators=n, random_state=42)
    rf.fit(X_train, y_train)
    y_pred = rf.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    print(f"n_estimators={n}, MSE={mse:.4f}")
