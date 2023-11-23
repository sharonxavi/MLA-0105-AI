import numpy as np

class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size

        # Initialize weights and biases
        self.weights_input_hidden = np.random.rand(self.input_size, self.hidden_size)
        self.bias_input_hidden = np.random.rand(1, self.hidden_size)
        self.weights_hidden_output = np.random.rand(self.hidden_size, self.output_size)
        self.bias_hidden_output = np.random.rand(1, self.output_size)

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def sigmoid_derivative(self, x):
        return x * (1 - x)

    def forward_pass(self, inputs):
        # Input to hidden layer
        hidden_inputs = np.dot(inputs, self.weights_input_hidden) + self.bias_input_hidden
        hidden_outputs = self.sigmoid(hidden_inputs)

        # Hidden to output layer
        output_inputs = np.dot(hidden_outputs, self.weights_hidden_output) + self.bias_hidden_output
        output = self.sigmoid(output_inputs)

        return output

    def train(self, inputs, targets, epochs, learning_rate):
        for epoch in range(epochs):
            # Forward pass
            hidden_inputs = np.dot(inputs, self.weights_input_hidden) + self.bias_input_hidden
            hidden_outputs = self.sigmoid(hidden_inputs)
            output_inputs = np.dot(hidden_outputs, self.weights_hidden_output) + self.bias_hidden_output
            outputs = self.sigmoid(output_inputs)

            # Calculate error
            output_error = targets - outputs

            # Backpropagation
            output_delta = output_error * self.sigmoid_derivative(outputs)
            hidden_error = np.dot(output_delta, self.weights_hidden_output.T)
            hidden_delta = hidden_error * self.sigmoid_derivative(hidden_outputs)

            # Update weights and biases
            self.weights_hidden_output += learning_rate * np.dot(hidden_outputs.T, output_delta)
            self.bias_hidden_output += learning_rate * np.sum(output_delta, axis=0, keepdims=True)
            self.weights_input_hidden += learning_rate * np.dot(inputs.T, hidden_delta)
            self.bias_input_hidden += learning_rate * np.sum(hidden_delta, axis=0, keepdims=True)

# Example usage
input_size = 2
hidden_size = 3
output_size = 1
nn = NeuralNetwork(input_size, hidden_size, output_size)

# Sample inputs and targets
inputs = np.array([[0, 1], [1, 0], [1, 1], [0, 0]])
targets = np.array([[1], [1], [0], [0]])

# Training the neural network
nn.train(inputs, targets, epochs=10000, learning_rate=0.1)

# Making predictions
predicted = nn.forward_pass(inputs)
print("Predicted:", predicted)
