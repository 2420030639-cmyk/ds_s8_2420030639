from sklearn.neighbors import KNeighborsClassifier
import numpy as np
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix


def main():
    X_train = np.array([[2,50], [3,60], [4,65], [5,70], [6,75], [7,80], [8,85], [9,90]])
    y_train = np.array([0,0,0,1,1,1,1,1])  # 0=Fail, 1=Pass
    X_test = np.array([[3,55], [5,72], [8,88], [4,60]])
    y_test = np.array([0,1,1,0])

    # Train the classifier\nmodel = KNeighborsClassifier(n_neighbors=3)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    error_rate = 1 - accuracy
    precision = precision_score(y_test, y_pred, zero_division=0)
    recall = recall_score(y_test, y_pred, zero_division=0)
    f1 = f1_score(y_test, y_pred, zero_division=0)
    cm = confusion_matrix(y_test, y_pred)

    print("Actual Labels:", y_test)
    print("Predicted Labels:", y_pred)
    print("Confusion Matrix:\\n", cm)
    print("Accuracy:", accuracy)
    print("Error Rate:", error_rate)
    print("Precision:", precision)
    print("Recall:", recall)
    print("F1-Score:", f1)


if __name__ == "__main__":
    main()
