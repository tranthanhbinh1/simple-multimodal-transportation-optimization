# (S) to 4 end_points (D1, D2, D3, and D4) through 2 distribution mid_points (N1 and N2).
# User input
import itertools
suppliers = {'S'}
good_types = {'A', 'B'}
end_points = {'D1', 'D2', 'D3', 'D4'}
middle_points = {'N1', 'N2'}

variables1 = []
for type in good_types:
    for sup in suppliers:
        for mid_point in middle_points:
            variables1.append(f'{type}_{sup}_{mid_point}')
            for end_point in end_points:
                variables1.append(f'{type}_{mid_point}_{end_point}')

supp_to_dis = list('_'.join(chars) for chars in itertools.product(good_types, suppliers, middle_points))
dis_to_hos = list('_'.join(chars) for chars in itertools.product(good_types, middle_points, end_points))
# Add to Variables
all_paths = set(supp_to_dis + dis_to_hos)

print(f"The total number of Paths that needs to be considered: {len(all_paths)}")

cost_of_each_path = []
for i in all_paths:
  cost_inp = int(input(f"Cost of {i}:"))
  cost_of_each_path.append(cost_inp)

# problem.objective.set_linear(list(costs.items()))
costs1 = dict(zip(all_paths, cost_of_each_path))
print(costs1)

# Supply constraints
supply_constraints1 = {}
for vacc_type in good_types:
    supply_key = vacc_type
    supply_value = [[f'{vacc_type}_S_{mid_point}' for mid_point in middle_points], [1, 1]]
    supply_constraints1[supply_key] = supply_value
print(f"Supply constraints are {supply_constraints1}")
# Demand RHS
supply_rhs = {}
for key in supply_constraints1:
    value = input(f"Enter supply value for each: '{key}': ")
    supply_rhs[key] = value
supply_rhs_list = []
for key,value in supply_rhs.items():
    supply_rhs_list.append(value)
print(f"Supply RHS are {supply_rhs_list}")

# Demand constraints
demand_constraints1 = {}
for point in end_points:
    for vacc_type in good_types:
        demand_key = f'{point}_{vacc_type}'
        demand_value = [[f'{vacc_type}_{mid_point}_{point}' for mid_point in middle_points], [1, 1]]
        demand_constraints1[demand_key] = demand_value
print(f"Demand constraints are {demand_constraints1}")

# Demand RHS
demand_rhs = {}
for key in demand_constraints1:
    value = input(f"Enter demand value for each pair '{key}': ")
    demand_rhs[key] = value
demand_rhs_list = []
for key,value in demand_rhs.items():
    demand_rhs_list.append(value)

print(f"Demand RHS is {demand_rhs_list}")


# Capacity Constraints
capacity_constraints1 = {}
for sup in suppliers:
    for dis in middle_points:
        constraint_key = f"{sup}_{dis}"
        constraint_value = [[f"{vacc}_{sup}_{dis}" for vacc in good_types], [1, 1]]
        capacity_constraints1[constraint_key] = constraint_value
for sup in suppliers:
    for dis in middle_points:
        # Create capacity constraints for each distribution mid_point
        for hosp in end_points:
            constraint_key = f"{dis}_{hosp}"
            constraint_value = [[f"{vacc}_{dis}_{hosp}" for vacc in good_types], [1, 1]]
            capacity_constraints1[constraint_key] = constraint_value
print(capacity_constraints1)

# Capacity RHS
capacity_rhs = {}
for key in capacity_constraints1:
    value = input(f"Enter capacity constraints for each pair '{key}': ")
    capacity_rhs[key] = value
capacity_rhs_list = []
for key,value in capacity_rhs.items():
    capacity_rhs_list.append(value)

print(f"Capacity RHS are {capacity_rhs_list}")

if __name__ == '__main__':
    print("User Input")
    print(f"suppliers: {suppliers}")
    print(f"type Types: {good_types}")
    print(f"end_points: {end_points}")
    print(f"Distribution mid_points: {middle_points}")
    print(f"Variables: {variables1}")
    print(f"Costs: {costs1}")
    print(f"Supply Constraints: {supply_constraints1}")
    print(f"Supply RHS: {supply_rhs_list}")
    print(f"Demand Constraints: {demand_constraints1}")
    print(f"Demand RHS: {demand_rhs_list}")
    print(f"Capacity Constraints: {capacity_constraints1}")
    print(f"Capacity RHS: {capacity_rhs_list}")