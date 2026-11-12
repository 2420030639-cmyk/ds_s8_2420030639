import numpy as np
from sklearn.linear_model import LinearRegression


def main():
    X = np.array([[1000], [1200], [1500], [1800], [2000]])
    y = np.array([50, 55, 65, 80, 90])

    model = LinearRegression()
    model.fit(X, y)
    new_house = np.array([[1700]])
    prediction = model.predict(new_house)

    print("Linear Regression - House Price Prediction")
    print("Training house sizes:", X.flatten())
    print("Training prices:", y)
    print("Slope:", model.coef_[0])
    print("Intercept:", model.intercept_)
    print("Predicted price for 1700 sq.ft house:", prediction[0], "lakhs")


if __name__ == "__main__":
    main()
