# Numerical Calculation of the Inverse Geometric Model (IGM) for a RRR Robot - TP1

## Description
This project aims to numerically compute the Inverse Geometric Model (IGM) of a RRR (Rotation-Rotation-Rotation) robot. The inverse geometric model is essential for robot control as it allows determining the joint angles needed to achieve a desired position and orientation in space.

## Objectives
- Implement multiple methods to find solutions for the IGM and compare their performance.
- Define exit conditions based on a maximum number of iterations and an error threshold for the objective function.

## Methods
1. **Gradient Method**:
   - This method minimizes the criterion \( C(q) = \frac{1}{2} ||e||^2 \) where \( e = X_d - f(q) \).
   - Here, \( X_d \) is the desired position, and \( f(q) \) is the direct kinematics function.

2. **Newton's Method**:
   - Uses a scheme to find the zero of the function \( H(q) = X_d - f(q) \).
   - This method requires calculating the derivative of the function \( f(q) \).

---

# TP Identification of Parameters of a RRR Robot Using Least Squares Techniques - TP2

## Description
The objective is to identify certain geometric parameters of the planar RRR robot using measurements obtained by a camera.

## Data Format
The results are found in the file `mesuresX.dat`. Each line contains the angle values \( q1, q2, q3 \) and the corresponding results of the direct kinematics model \( mgd(q) \), which includes \( x, y, θ \).

## Tasks
1. **Identification of Link Lengths**:
   - Write the system of equations to calculate the lengths \( l1, l2, l3 \).
   - Write the residual corresponding to a measurement.
   - Formulate the problem as Linear Least Squares (LLS) and implement the solution calculation.
   - Verify that your solution matches the values from the measurement file.

2. **Identification of Link Lengths and Encoder Offset**:
   - Write the system of equations to calculate \( l1, l2, d \) considering \( l3 = 10 \).
   - Model the new problem as LLS and modify the program to compute the solution.
   - Verify that your solution matches the values from the measurement file.

3. **Using `scipy.optimize`**:
   - Use the `least_squares` function to calculate the solution.
   - Compare the values obtained with those from the previous section.

---

# TP Optimization of Robot Placement - TP3

## Description
To perform a robotic task, it is necessary to position three robots in a workshop. The position of the robots forms a triangle, and the goal is to maximize the area of this triangle.

## Robots
- **STAUBLI**: working radius = 1000 mm
- **MITSUBISHI**: working radius = 2000 mm
- **EPSON**: working radius = 750 mm

## Tasks
1. **Work**:
   - Define the variables of the problem.
   - Write the function to minimize/maximize.
   - Define the constraints.
   - Use `scipy.optimize` to solve the placement problem.
   - Display the results, including the positions of the robots and the trajectory of the bus.

