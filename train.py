from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
import joblib
import os

iris = load_iris()
X, y = iris.data, iris.target

model = LogisticRegression(max_iter=200)
model.fit(X, y)

os.makedirs("model", exist_ok=True)
joblib.dump(model, "model/iris_model.pkl")
print("✅ Model trained and saved.")
