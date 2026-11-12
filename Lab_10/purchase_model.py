import numpy as np
from sklearn.linear_model import LogisticRegression


def main():
    X = np.array([[40], [50], [60], [70], [80], [90]])
    y = np.array([0, 0, 0, 1, 1, 1])  # 0=Not Purchased, 1=Purchased

    model = LogisticRegression()
    model.fit(X, y)
    test_price = np.array([[75]])
    prediction = model.predict(test_price)
    probability = model.predict_proba(test_price)

    print("Logistic Regression - House Purchase Classification")
    print("Test house price:", test_price[0, 0], "lakhs")
    print("Purchase prediction:", prediction[0])
    print("Prediction probabilities:", probability)


if __name__ == "__main__":
    main()
