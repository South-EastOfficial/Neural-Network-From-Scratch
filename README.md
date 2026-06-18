# Neural-Network-From-Scratch
# Neural Network From Scratch

## Overview

This project implements a feedforward neural network from scratch using Python and NumPy without relying on machine learning frameworks such as TensorFlow, PyTorch, or Keras.

The goal of this project was to understand the mathematical foundations of neural networks by implementing every major component manually, including forward propagation, backpropagation, gradient descent, activation functions, and loss calculation.

---

## Features

* Sigmoid activation function
* Mean Squared Error (MSE) loss
* Forward propagation
* Backpropagation
* Gradient descent optimization
* Weight and bias updates
* Binary classification example

---

## Project Structure

```text
src/
├── first_neuron.py
├── simple_network.py
├── mse_loss.py
└── neural_network_training.py
```

### first_neuron.py

Implements a single artificial neuron using:

* Weights
* Bias
* Sigmoid activation function

### simple_network.py

Builds a small neural network consisting of:

* Two input neurons
* One hidden layer
* One output neuron

Demonstrates the feedforward process.

### mse_loss.py

Implements Mean Squared Error (MSE), a common loss function used to measure prediction error.

### neural_network_training.py

Complete neural network implementation including:

* Forward propagation
* Loss calculation
* Backpropagation
* Gradient descent
* Model training

---

## Technologies Used

* Python
* NumPy

---

## Concepts Implemented

### Forward Propagation

Input values are passed through weighted connections and activation functions to generate predictions.

### Sigmoid Activation Function

The sigmoid function maps values to the range:

f(x) = 1 / (1 + e^(-x))

allowing the network to model non-linear relationships.

### Loss Function

Mean Squared Error (MSE) is used to measure prediction accuracy.

### Backpropagation

Gradients are calculated using the chain rule and propagated backward through the network to update parameters.

### Gradient Descent

Weights and biases are adjusted iteratively to minimize prediction error.

---

## Learning Outcomes

Through this project, I gained practical experience with:

* Neural network architecture
* Activation functions
* Loss functions
* Gradient descent
* Backpropagation
* Machine learning fundamentals
* Mathematical foundations of deep learning

---

## Future Improvements

* Support for multiple hidden layers
* Additional activation functions (ReLU, Tanh)
* Mini-batch gradient descent
* Multi-class classification
* Visualization of training progress

---

## Author

Shivam Maurya

Built as a learning project to understand neural networks from first principles.
