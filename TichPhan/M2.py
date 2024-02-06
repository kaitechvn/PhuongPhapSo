import math

import numpy as np

def f(x):
    # Define your function here
    return pow(x,2.7)

def second_order_derivative(x, h):
    # Calculate the second-order derivative of the function
    return (f(x + h) - 2*f(x) + f(x - h))/(h**2)

# Define the interval [a, b]
a = 0
b = 1

# Define the step size h
h = 0.000001

# Create an array of values for x in the interval [a, b]
x_values = np.arange(a, b, h)

# Calculate the second-order derivative of the function for each value of x
second_order_derivatives = [second_order_derivative(x, h) for x in x_values]

# Find the maximum value of the second-order derivative
max_second_order_derivative = max(map(abs, second_order_derivatives))

print("The maximum value of the second-order derivative of the function on the interval [{}, {}] is {}.".format(a, b, max_second_order_derivative))
