from pulp import LpMaximize, LpProblem, LpVariable, lpSum, LpStatus

# Define the problem
problem = LpProblem(name="production-optimization", sense=LpMaximize)

# Decision variables for the number of units to produce
x_A = LpVariable(name="Product_A", lowBound=0, cat="Continuous")
x_B = LpVariable(name="Product_B", lowBound=0, cat="Continuous")

# Objective function: Maximize profit
profit = 40 * x_A + 30 * x_B
problem += profit

# Constraints
problem += (2 * x_A + 3 * x_B <= 60, "Labor Constraint")
problem += (3 * x_A + 2 * x_B <= 50, "Material Constraint")

# Solve the problem
status = problem.solve()

# Output results
print(f"Status: {LpStatus[problem.status]}")
print(f"Optimal Solution: Product A = {x_A.value()}, Product B = {x_B.value()}")
print(f"Maximum Profit: ${problem.objective.value()}")
import matplotlib.pyplot as plt
import numpy as np

# Generate plots for constraints
labor_constraint = lambda x: (60 - 2 * x) / 3
material_constraint = lambda x: (50 - 3 * x) / 2

x_vals = np.linspace(0, 30, 500)
plt.plot(x_vals, labor_constraint(x_vals), label="Labor Constraint")
plt.plot(x_vals, material_constraint(x_vals), label="Material Constraint")
plt.fill_between(x_vals,
                 np.minimum(labor_constraint(x_vals), material_constraint(x_vals)),
                 color='gray', alpha=0.2, label="Feasible Region")

plt.scatter(x_A.value(), x_B.value(), color='red', label='Optimal Solution')

plt.xlabel('Product A')
plt.ylabel('Product B')
plt.legend()
plt.title('Feasible Region and Optimal Solution')
plt.grid()
plt.show()
