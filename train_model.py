import numpy as np
from sklearn.svm import SVC
import joblib


X = np.random.randint(0, 2000, size=(500, 20))


y = np.random.randint(0, 4, size=(500,))


model = SVC()


model.fit(X, y)


joblib.dump(model, "best_svc_model.pkl")

print("Model saved successfully!")