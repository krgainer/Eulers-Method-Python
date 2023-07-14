import numpy as np
import csv
from math import sin, pi, exp

# Define the derivative function for the problem
def derivativeFunction(t, y):
    return t**2 * y + sin(2*pi*t)

# Define the different step sizes to be used in Euler's method
h_values = [0.1, 0.01, 0.001, .0001]

# Define initial conditions, ranges and derivative functions for each problem
problem_name = 'example'  # Name of the problem, for saving purposes
problem = {"y0": 1, "t0": 0, "tf": 2, "dydt": derivativeFunction}  # Problem parameters


# --------------------------------------------


# Define Euler's method for numerical integration
def euler_method(dydt, y0, t0, tf, h):
    results = []  # Initialize the output string
    y = y0  # Initialize y with the initial condition
    t = t0  # Initialize t with the start time
    while t <= tf:  # Loop until end time is reached
        y = y + h * dydt(t, y)  # Update y using Euler's method
        results.append({"t": format(t, '.10f'), "y": format(y, '.10f')})  # Store the current time and y value, to 10 decimal places for both.
        t += h  # Increment the time by the step size h
    return results  # Return the results list

# Solve the problemS using Euler's method
for h in h_values:  # Loop over the different step size
    # Print the results for each problem and step size
    results = euler_method(**problem, h=h)
    # Write the results to a CSV file
    with open(f'problem_{problem_name}_h_{h}.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=["t", "y"])
        writer.writeheader()
        writer.writerows(results)
