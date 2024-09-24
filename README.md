# README

## Numerical Calculation of the Inverse Geometric Model (IGM) for a RRR Robot

### Description
This project aims to numerically compute the Inverse Geometric Model (IGM) of a RRR robot.

### Objectives
- Implement multiple methods to find solutions for the IGM and compare their performance.
- Define exit conditions based on a maximum number of iterations and an error threshold for the objective function.

### Methods
1. **Gradient Method**: Minimize the criterion \( C(q) = \frac{1}{2} \; ||e||^2 \) with \( e = X_d - f(q) \).
2. **Newton's Method**: Use the scheme to find the zero of the function \( H(q) = X_d - f(q) \).
