import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest

rng = np.random.RandomState(42)

X = 0.3 * rng.randn(100, 2)
X_train = np.r_[X + 2, X - 2]

X_outliers = rng.uniform(low=-4, high=4, size=(20, 2))

X_all = np.r_[X_train, X_outliers]

model = IsolationForest(contamination=0.1, random_state=42)
model.fit(X_all)

y_pred = model.predict(X_all)

plt.figure(figsize=(8, 6))
plt.scatter(X_all[y_pred == 1, 0], X_all[y_pred == 1, 1], c='blue', label='Normal')
plt.scatter(X_all[y_pred == -1, 0], X_all[y_pred == -1, 1], c='red', label='Anomaly')
plt.legend()
plt.title("Isolation Forest Anomaly Detection")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.grid(True)
plt.show()
