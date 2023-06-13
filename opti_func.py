import cplex
from user_input import (variables1, costs1, supply_constraints1, 
                        demand_constraints1, capacity_constraints1, 
                        supply_rhs_list, demand_rhs_list, capacity_rhs_list)

def solve_optimization(variables, costs, supply_constraints, demand_constraints, capacity_constraints, supply_rhs, demand_rhs, capacity_rhs):
    # Initialize the problem
    problem = cplex.Cplex()


    problem.objective.set_sense(problem.objective.sense.minimize)

    # Define the variables and their types

    problem.variables.add(names=variables, types=[problem.variables.type.continuous] * len(variables))

    # Set the objective function
    problem.objective.set_linear(list(costs.items()))

    # Add the supply constraints
    problem.linear_constraints.add(
        lin_expr=[cplex.SparsePair(ind=supply_constraints[v][0], val=supply_constraints[v][1]) for v in ['A', 'B']],
        senses=["E", "E"],
        rhs=[float(num) for num in supply_rhs],
        names=[f"Supply_{key}" for key in supply_constraints.keys()]
    )

    # Add the demand constraints
    problem.linear_constraints.add(
        lin_expr=[cplex.SparsePair(ind=demand_constraints[v][0],

    val=demand_constraints[v][1]) for v in demand_constraints.keys()],
        senses=["E"] * len(demand_constraints),
        rhs=[float(num) for num in demand_rhs],
        names=list(demand_constraints.keys())
    )

    # Add the capacity constraints
    problem.linear_constraints.add(
        lin_expr=[cplex.SparsePair(ind=capacity_constraints[v][0], val=capacity_constraints[v][1]) for v in capacity_constraints.keys()],
        senses=["L"] * len(capacity_constraints),
        rhs=[float(num) for num in capacity_rhs],
        names=list(capacity_constraints.keys())
    )

    # Solve the problem
    problem.solve()

    # Print the solution status
    print("Solution status = ", problem.solution.get_status(), ":", end=' ')
    print(problem.solution.status[problem.solution.get_status()])

    # Print the solution value
    print("Solution value  = ", problem.solution.get_objective_value())

    # Get the optimal values for the decision variables
    x = problem.solution.get_values()
    for v, val in zip(variables, x):
        if val > 0:
            print(f'{v}: {val}')
        else:
            pass


if __name__ == '__main__':
   solve_optimization(variables1, costs1, supply_constraints1, demand_constraints1, capacity_constraints1, supply_rhs_list, demand_rhs_list, capacity_rhs_list)