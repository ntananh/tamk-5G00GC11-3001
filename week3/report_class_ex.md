Note:

Run Result:
DecisionTreeRegressor Results:
max_depth=1, MSE=18347.6241
max_depth=3, MSE=11911.9376
max_depth=5, MSE=11914.6612
max_depth=None, MSE=11914.6612


RandomForestRegressor Results:
n_estimators=1, MSE=25259.6109
n_estimators=20, MSE=5531.8010
n_estimators=100, MSE=5524.6990


## Decision Tree
max_depth=1 -> MSE 18347 -> underfitting: the tree is too shallow to capture patterns.
max_depth=3 -> MSE 11912 -> significant improvement; model captures main trends.
max_depth=5 / None -> MSE 11915 -> little or no improvement, suggesting the data size or features limits further gain; deeper trees may overfit but test set is not showing much difference.

So: Depth beyond 3 does not improve performance much. A shallow tree already captures the main signal.

## Random Forest
n_estimators=1 -> MSE 25260 -> single tree performs worse than optimized Decision Tree.
n_estimators=20 -> MSE 5532 -> huge improvement and  averaging many trees reduces variance.
n_estimators=100 → MSE 5525 → slight further improvement and adding more trees yields diminishing returns.

Why?: Random Forests reduce overfitting and variance. Even with moderate number of trees (20), performance is much better than any single tree.


## Besides max_depth and n_estimators, the following affect prediction quality:

Data Quality
    Missing values
Feature Engineering
    Relevant features improve predictions
    Scaling is not required for trees but can matter for comparisons with other models
Hyperparameters
    min_samples_split, min_samples_leaf, max_features (Random Forest)
    bootstrap sampling
Randomness
    Random seed (random_state) affects reproducibility
Training Set Size
    More data → generally better generalization
Correlation & Redundancy
    Highly correlated features in Random Forests reduce diversity among trees