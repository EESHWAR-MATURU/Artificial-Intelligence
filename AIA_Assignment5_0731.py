import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation
from tensorflow.keras.optimizers import Adam

X, y = make_moons(n_samples=1000, noise=0.1, random_state=0)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=0)


def create_model(input_shape, hidden_layers, output_shape, learning_rate):
    model = Sequential()
    model.add(Dense(hidden_layers[0], input_shape=input_shape))
    model.add(Activation('relu'))
    for i in range(1, len(hidden_layers)):
        model.add(Dense(hidden_layers[i]))
        model.add(Activation('relu'))
    model.add(Dense(output_shape))
    model.add(Activation('sigmoid'))
    optimizer = Adam(learning_rate=learning_rate)
    model.compile(optimizer=optimizer,
                  loss='binary_crossentropy', metrics=['accuracy'])
    return model

input_shape = (2,)
hidden_layers = [(64,), (128,), (256,), (64, 32), (128, 64)]
output_shape = 1
learning_rates = [0.001, 0.01, 0.1]


for hl in hidden_layers:
    for lr in learning_rates:
        model = create_model(input_shape, hl, output_shape, lr)
        history = model.fit(X_train, y_train, validation_data=(
            X_test, y_test), epochs=50, batch_size=32, verbose=0)
        score = model.evaluate(X_test, y_test, verbose=0)
        print(
            f"Hidden Layers: {hl}, Learning Rate: {lr}, Test Loss: {score[0]}, Test Accuracy: {score[1]}")

        x_min, x_max = X[:, 0].min() - 0.5, X[:, 0].max() + 0.5
        y_min, y_max = X[:, 1].min() - 0.5, X[:, 1].max() + 0.5
        xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.1),
                             np.arange(y_min, y_max, 0.1))
        Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
        Z = np.round(Z)
        Z = Z.reshape(xx.shape)
        plt.contourf(xx, yy, Z, cmap=plt.cm.RdBu, alpha=0.8)
        plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.RdBu)
        plt.title(
            f"Hidden Layers: {hl}, Learning Rate: {lr}, Test Accuracy: {score[1]:.2f}")
        plt.show()
