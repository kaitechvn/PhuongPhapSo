import math
from sympy import sympify, symbols


from sympy import symbols, diff, lambdify
import numpy as np

# Define the variable
x = symbols('x')

# Define the function
func = input('Nhập hàm f(x): ')
f = sympify(func)

# Calculate the fourth derivative
fourth_derivative = diff(f, x, 2)


# Lambdify the fourth derivative
fourth_derivative_func = lambdify(x, fourth_derivative, "numpy")

# Create an array of x values from 0 to 1
x_values = np.linspace(0.1, 1, 100)

# Evaluate the fourth derivative at each x value
fourth_derivative_values = fourth_derivative_func(x_values)

# Find the absolute maximum of the fourth derivative values
abs_max = np.max(np.abs(fourth_derivative_values))

# Print the absolute maximum
print(abs_max)
