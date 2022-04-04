import numpy as np
import copy

# We should define a class for storing the problem information, including Variables, Domains and Constraints
class CSP:
  def __init__(self, variables, domains, constraints):
    self.variables = variables
    self.domains = domains
    self.constraints = constraints
    

def backtracking_search(csp):
  # Initialize a dictionary assignment
  assignment = {}
  for v in csp.variables:
    assignment[v] = None  # {R1: None, R2: None, ..., R4:None}
  return backtracking(assignment, csp)

def backtracking(assignment, csp):
  if complete(assignment, csp):
    print("We have found a complete solution")
    return assignment
  else:
    var = select_unassigned_variable(csp, assignment)
    print("*Selected variable: ", var)
    inferences = {}
    for value in order_domain_values(var, assignment, csp):
      print("\t**Trying: ", value)
      original_domain = copy.deepcopy(csp.domains)
      print("Current domains: ", original_domain)
      if is_consistent(value, var, assignment, csp):
        print("\t{} is consistent with current assignment.".format(value))
        # Assign value, therefore modify domain in csp
        assignment[var] = value
        csp.domains[var] = [value] # We assign directly the singleton domain
        
        #inferences = no_inference(csp, var, value)
        inferences = inference(csp, var, value, assignment)
        print("\tInferences: ", inferences)
        print("\tDomains after inference: ", csp.domains)
        if inferences is not None:
          # Add to assignment
          for k, v in inferences.items():
            assignment[k] = v
          print("-------Recurring...")
          result = backtracking(assignment, csp)
          if result:
            return result
      # remove explored values from assignment and restore the domains
      print("\tBACKTRACK!")
      assignment[var] = None
      if inferences is not None or len(inferences)>0:
        for k, v in inferences.items():
            assignment[k] = None
      csp.domains = copy.deepcopy(original_domain)
      print("\tRestored domains: ", csp.domains)
    return None

# Test for a complente and legal solution
def complete(assignment, csp):
  for v in list(assignment.values()):
    if not v:
      return False
  for constraint in csp.constraints:
    values = []    
    for v in constraint['scope']:
      values.append(assignment[v])
    result = constraint['rel'](*values)
    if not result:
      return False
  return True

# Check consistency of  the solution
def is_consistent(value, var, assignment, csp):
  # test all constraints for given assignment
  a = copy.deepcopy(assignment)
  a[var] = value
  print("\tTesting ", a)
  for constraint in csp.constraints:
    values = []    
    for v in constraint['scope']:
      values.append(a[v])
    result = constraint['rel'](*values)
    if not result:
      return False
  return True

# Simple implementation: Select the first unassigned variable that it founds
def select_unassigned_variable(csp, assignment):
  for k, v in assignment.items():
    if not v: # this happpens when we do not have a value assigned to the var k
      return k
  return None

# Leave them in the same order
def order_domain_values(var, assignment, csp):
  return csp.domains[var]

# for each unassigned variable Y that is connected to X (var in this case) by a constraint, 
# delete from Y ’s domain any value that is inconsistent with the value chosen for X
def inference(csp, var, value, assignment):
  print("\tInference from ", var)
  queue = []
  var_neighbors = []
  for constraint in csp.constraints:    
    Y = constraint['scope'][0]
    X = constraint['scope'][1]
    # Find unassigned neighbors from X and retrive their constraints
    if var == X and assignment[Y] is None:
      queue.append(constraint)
      var_neighbors.append(Y)
  # AC3
  #print("-----AC3 started-------")
  while len(queue)>0:
    #print("Current queue: ", queue)
    #print("Current queue: ", len(queue))
    constraint = queue.pop(0)
    Xi = constraint['scope'][0]
    Xj = constraint['scope'][1]
    if revise_constraint(csp, constraint):
      if len(csp.domains[Xi])==0:
        print("Found an empty domain, no solution ahead!")
        return None
      #print("Since the domain of {} changed, we will check consistency in its neighbors.".format(Xi))
      queue = neighbors(Xi, Xj, csp) + queue
  #print("-----AC3 finished-------")
  
  # retrive assignment of singleton domains
  results = {}
  for Y in var_neighbors:
    if len(csp.domains[Y])==1:
      results[Y] = csp.domains[Y][0]
  return results

def no_inference(csp, var, value):
  return {}

def revise_constraint(csp, constraint):
  revised = False
  Xi = constraint['scope'][0]
  Xj = constraint['scope'][1]
  rel = constraint['rel']
  #print("Variable 1: ", Xi)
  #print("Variable 2: ", Xj)
  #print("Domain 1: ", csp.domains[Xi])
  #print("Domain 2: ", csp.domains[Xj])
  for x in csp.domains[Xi]:
    #print("\n\tValidating ", x)
    at_leats_one_satisfied = False
    for y in csp.domains[Xj]:
      #print("\t\tAgainst ", y)
      satisfied = rel(x,y)
      #print("\t\tResult: ", satisfied)
      if satisfied:
        at_leats_one_satisfied = True
    if not at_leats_one_satisfied:
      revised = True
      csp.domains[Xi].remove(x)
      #print("\t{} is remove from domain in {}".format(x, Xi))
  return revised

# This function returns neighboring constraints to the given variable1 without variable2
def neighbors(variable1, variable2, csp):
  neighboring_constraints = []
  for constraint in csp.constraints:
    if constraint['scope'][1] == variable1 and constraint['scope'][0] != variable2: # This means that this constraint is a neighbor from variable1
      neighboring_constraints.append(constraint)
  return neighboring_constraints


# Define variables and domains as a dict 
variables_list = ['R1', 'R2', 'R3', 'R4', 'R5', 'R6', 'R7', 'R8', 'R9', 'R10', 'R11', 'R12', 'R13', 'R14', 'R15', 'R16', 'R17', 'R18']

domains_dict =   { 'R1':['red','green', 'blue', 'orange'],
                   'R2':['red','green', 'blue', 'orange'],
                   'R3':['red','green', 'blue', 'orange'],
                   'R4':['red','green', 'blue', 'orange'],
                   'R5':['red','green', 'blue', 'orange'],
                   'R6':['red','green', 'blue', 'orange'],
                   'R7':['red','green', 'blue', 'orange'],
                   'R8':['red','green', 'blue', 'orange'],
                   'R9':['red','green', 'blue', 'orange'],
                  'R10':['red','green', 'blue', 'orange'],
                  'R11':['red','green', 'blue', 'orange'],
                  'R12':['red','green', 'blue', 'orange'],
                  'R13':['red','green', 'blue', 'orange'],
                  'R14':['red','green', 'blue', 'orange'],
                  'R15':['red','green', 'blue', 'orange'],
                  'R16':['red','green', 'blue', 'orange'],
                  'R17':['red','green', 'blue', 'orange'],
                  'R18':['red','green', 'blue', 'orange']}


# Define constraints as functions -------------
def not_equal(v1, v2):
  if not v1 and not v2:
    return True
  if not v1:
    return True
  if not v2:
    return True
  return v1 != v2

# Define scope (involved variables) and their constraints----
constraint_dict = [{'scope':('R1','R2'), 'rel': not_equal},
                   {'scope':('R1','R18'), 'rel': not_equal},
                   {'scope':('R2','R3'), 'rel': not_equal},
                   {'scope':('R3','R4'), 'rel': not_equal},
                   {'scope':('R2','R4'), 'rel': not_equal},
                   {'scope':('R2','R18'), 'rel': not_equal},
                   {'scope':('R13','R11'), 'rel': not_equal},
                   {'scope':('R18','R4'), 'rel': not_equal},
                   {'scope':('R4','R7'), 'rel': not_equal},
                   {'scope':('R4','R6'), 'rel': not_equal},
                   {'scope':('R18','R6'), 'rel': not_equal},
                   {'scope':('R18','R5'), 'rel': not_equal},
                   {'scope':('R5','R6'), 'rel': not_equal},
                   {'scope':('R6','R7'), 'rel': not_equal},
                   {'scope':('R8','R10'), 'rel': not_equal},
                   {'scope':('R7','R8'), 'rel': not_equal},
                   {'scope':('R5','R7'), 'rel': not_equal},
                   {'scope':('R5','R9'), 'rel': not_equal},
                   {'scope':('R7','R9'), 'rel': not_equal},
                   {'scope':('R7','R10'), 'rel': not_equal},
                   {'scope':('R9','R10'), 'rel': not_equal},
                   {'scope':('R8','R9'), 'rel': not_equal},
                   {'scope':('R11','R10'), 'rel': not_equal},
                   {'scope':('R11','R12'), 'rel': not_equal},
                   {'scope':('R12','R10'), 'rel': not_equal},
                   {'scope':('R12','R13'), 'rel': not_equal},
                   {'scope':('R13','R14'), 'rel': not_equal},
                   {'scope':('R14','R15'), 'rel': not_equal},
                   {'scope':('R15','R16'), 'rel': not_equal},
                   {'scope':('R16','R14'), 'rel': not_equal},
                   {'scope':('R16','R17'), 'rel': not_equal}]


# Execution of the searching algorithm

# Instantiate a CSP
problem = CSP(variables_list, domains_dict, constraint_dict)

# Check problem
result = backtracking_search(problem)
print(result)