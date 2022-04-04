import numpy as np

RO="RO"
AM="AM"
VE="VE"
AZ="AZ"
GR="GR"
NE="NE"
#This list will contain 6 lists, each of which will contain the state of a solved floppy rubik's cube.
solvedState=[[[RO,RO,RO],[RO,RO,RO],[RO,RO,RO]],
            [[AM,AM,AM],[AM,AM,AM],[AM,AM,AM]],
            [VE,VE,VE],
            [AZ,AZ,AZ],
            [GR,GR,GR],
            [NE,NE,NE]]


#This list will contain 6 lists, each of which will contain tha state of a scrambled floppy rubik's cube.
scrambledState=[[[AM,AM,AM],[AM,RO,RO],[RO,AM,RO]],
            [[AM,AM,AM],[AM,AM,AM],[AM,AM,AM]],
            [AZ,VE,VE],
            [VE,AZ,AZ],
            [GR,GR,GR],
            [NE,NE,NE]]

# We should define a class for storing the information about our nodes and states
class Node:
  def __init__(self, state, parent, action, path_cost):
    self.state = state
    self.parent = parent
    self.action = action
    self.path_cost = path_cost

# Define the actions-------------
def move_mm(state):
  action = np.array([-2, 0, -1])
  return state + action

def move_cc(state):
  action = np.array([0, -2, -1])
  return state + action

def move_mc(state):
  action = np.array([-1, -1, -1])
  return state + action

def return_m(state):
  action = np.array([1, 0, 1])
  return state + action

def return_c(state):
  action = np.array([0, 1, 1])
  return state + action

def return_mm(state):
  action = np.array([2, 0, 1])
  return state + action

def return_cc(state):
  action = np.array([0, 2, 1])
  return state + action

def return_mc(state):
  action = np.array([1, 1, 1])
  return state + action

actions_dict = {'move_mm': move_mm, 'move_cc': move_cc, 'move_mc': move_mc,
                'return_m': return_m, 'return_c': return_c, 
                'return_mm': return_mm, 'return_cc': return_cc, 'return_mc': return_mc}

# We should define a class problem.
# For this example we will use the missionaries and cannibals problem
class Problem:
  #--------------------------------
  def __init__(self, initial_state, goal_state, actions_dict):
    self.initial_state = initial_state
    self.goal_state = goal_state
    self.actions_dict = actions_dict
    self.solution = None
  
  # Given the state, we should return the available actions
  def actions(self, state):
    return list(actions_dict.keys())
  
  # It should return the resulting state of applying the action to the current state
  def results(self, state, action):
    r = self.actions_dict[action](state)
    
    # Validate result
    if np.any(r<0):
      print(np.array2string(r)+"is an action not valid\n")
      return None
    elif np.any(r[:2]>3):
      print(np.array2string(r)+"is an action not valid\n")
      return None
    elif r[2]>=2:
      print(np.array2string(r)+"is an action not valid\n")
      return None
    elif r[0]<r[1] and r[0]!=0: # More cannibals than missionaries before crossing is an invalid state
      print(np.array2string(r)+"is an action not valid\n")
      return None
    elif (3-r[0]) < (3-r[1]) and (3-r[0])!=0: # More cannibals than missionaries after crossing is an invalid state
      print(np.array2string(r)+"is an action not valid\n")
      return None
    else:
      return r

  # It should return true if the passed state is equal to the goal state
  def goal_test(self, state):
    return np.all(state == self.goal_state)
  
  # It should return the cost of executing certain action to go from state to next state.
  def step_cost(self, state, action, next_state):
    return 1

# Method for retriving the solution given the goal node.
def solution(node):
  s = [node]
  #print(s)
  if node.parent is None:
    return s
  else:
    return s + solution(node.parent)

# Method to expand a parent node into a child node
def child_node(problem, parent, action):
  child_state = problem.results(parent.state, action)
  if child_state is not None:
    node = Node(child_state, parent, action, problem.step_cost(parent.state, action, child_state) + parent.path_cost)
    return node
  else: 
    return None

# Auxiliar method to check if a state is on the frontier
def is_in_nodes(node_list, state):
  for n in node_list:
    if np.all(n.state == state):
      return True
  return False

# Search function (in this example we are using breadth-first search)
def bfs(problem):
  node = Node(problem.initial_state, None, None, 0)
  if problem.goal_test(node.state):
    return solution(node)
  frontier = [node]
  explored = []
  while len(frontier)>0:
    node = frontier.pop(0) # FIFO
    explored.append(node)
    print("------------")
    print("Current node state: ", node.state)
    for a in problem.actions(node.state):
      child = child_node(problem, node, a)
      if not child:
        continue 
      print("Action :", a)
      print("Child state: ", child.state)
      if not (is_in_nodes(explored, child.state) or is_in_nodes(frontier, child.state)):
        if problem.goal_test(child.state):
          print("Solution found!")
          s=solution(child)
          return 
        frontier.append(child)
      else:
        print("Node already explored!")
  return None

def dfs(problem):
  def DFSUtil(v, visited):

    # Mark the current node as visited
    # and print it
    visited.add(np.array2string(v.state))
    print("*********************************************")
    print("Current state: "+np.array2string(v.state)+"\n")
    # Recur for all the vertices
    # adjacent to this vertex

    for action in problem.actions(v):
      print("Action: ", action)
      neighbour = child_node(problem, v, action)
      if neighbour is not None:
        if np.array2string(neighbour.state) not in visited:
          if problem.goal_test(neighbour.state):
            print("Solution found!")
            return solution(neighbour)       
          print("Action accepted")
          return (DFSUtil(neighbour, visited))
        else:
          print("Node already explored!")
    return None
  
  node = Node(problem.initial_state, None, None, 0)

  if problem.goal_test(node.state):
    return solution(node)
  
  visited = set()
  return DFSUtil(node,visited)

# Set initial state and goal state
p = Problem(np.array([3,3,1]), np.array([0,0,0]), actions_dict)

# Search for solution
sol = dfs(p)
flag=0

# Show solution
for s in sol[::-1]:
  print("{} -> {}".format(s.action, s.state))