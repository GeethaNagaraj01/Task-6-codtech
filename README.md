Name: Geetha N
Company:CODETECH IT SOLUTIONS 
ID:CT0806EK Domain: DATA SCIENCE
Duration:December 12th,2024 to january 12th,2025 
Mentor: Neha

OVERVIEW OF THE PROJECT

OPTIMIZATION MODEL

Objective
The goal of this project is to determine the optimal number of two products (Product A and Product B) that a company should produce to maximize profit while staying within the constraints of labor and material availability.

Problem Statement
A company produces two products:

Product A yields a profit of $40 per unit.
Product B yields a profit of $30 per unit.
Constraints:

Labor:

Each unit of Product A requires 2 hours.
Each unit of Product B requires 3 hours.
The total available labor is 60 hours.
Material:

Each unit of Product A requires 3 units of material.
Each unit of Product B requires 2 units of material.
The total available material is 50 units.
Business Question:
How many units of Product A and Product B should the company produce to maximize profit while adhering to the resource constraints?

Solution Approach
The problem was modeled and solved using Linear Programming (LP) with the PuLP library in Python.

Steps:
Define Decision Variables:

𝑥
𝐴
x 
A
​
 : Number of units of Product A to produce.
𝑥
𝐵
x 
B
​
 : Number of units of Product B to produce.
Objective Function:

Maximize: 
𝑍
=
40
⋅
𝑥
𝐴
+
30
⋅
𝑥
𝐵
Maximize: Z=40⋅x 
A
​
 +30⋅x 
B
​
 
Where 
𝑍
Z is the total profit.

Constraints:

Labor: 
2
⋅
𝑥
𝐴
+
3
⋅
𝑥
𝐵
≤
60
2⋅x 
A
​
 +3⋅x 
B
​
 ≤60
Material: 
3
⋅
𝑥
𝐴
+
2
⋅
𝑥
𝐵
≤
50
3⋅x 
A
​
 +2⋅x 
B
​
 ≤50
Non-negativity: 
𝑥
𝐴
≥
0
,
𝑥
𝐵
≥
0
x 
A
​
 ≥0,x 
B
​
 ≥0
Solve Using PuLP:

Use PuLP’s optimization solver to find the optimal values of 
𝑥
𝐴
x 
A
​
  and 
𝑥
𝐵
x 
B
​
 Analyze Result

Optimal production quantities for Product A and Product B.
Maximum achievable profit.
Verify constraints are satisfied.
Tools and Libraries
Programming Language: Python
Optimization Library: PuLP
Visualization Library: Matplotlib (optional, for feasible region and solution plot)
Development Environment: PyCharm Professional
Results
Optimal Solution: The number of units for Product A and Product B to produce.
Maximum Profit: The highest profit achievable under the given constraints.
Feasibility: The solution satisfies all labor and material constraints.
Deliverables
Python Script:
A standalone script (optimization.py) that models and solves the problem.
Documentation:
Inline comments explaining the code.
Visualization (Optional):
A plot showing the feasible region and the optimal solution.
Insights
The project provides a systematic method for maximizing profit under resource constraints.
Insights into resource utilization and how constraints impact decision-making.
Scalability: The model can easily be adapted to more complex problems (e.g., more products, additional constraints).
Next Steps or Extensions
Complex Problems: Include additional constraints like storage, transportation costs, or machine availability.
Sensitivity Analysis: Analyze the impact of changes in resources or profits.
Deployment: Package the solution as an API using Flask or FastAPI for interactive use.


![image](https://github.com/user-attachments/assets/5906c766-b9cb-4085-8801-a858d2084abe)

![image](https://github.com/user-attachments/assets/d27d604b-f19d-41a7-bfd8-910149d3a215)


