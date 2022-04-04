import numpy as np

# We should define a class for storing the information about our nodes and states
class Node:
  def __init__(self, state, parent, action, path_cost):
    self.state = state
    self.parent = parent
    self.action = action
    self.path_cost = path_cost



# Define the actions-------------
def move_lv(state):

    if state[0,0] > state[5,0]:
        pos00 = -1
        pos50 = 1
    elif state[0,0] < state[5,0]:
        pos00 = 1
        pos50 = -1
    else:
        pos00 = 0
        pos50 = 0

    if state[2,0] > state[2,2]:
        pos20 = -1
        pos22 = 1
    elif state[2,0] < state[2,2]:
        pos20 = 1
        pos22 = -1
    else:
        pos20 = 0
        pos22 = 0

    if state[1,0] > state[4,6]:
        pos10 = -1
        pos46 = 1
    elif state[1,0] < state[4,6]:
        pos10 = 1
        pos46 = -1
    else:
        pos10 = 0
        pos46 = 0

    if state[1,3] > state[4,3]:
        pos13 = -1
        pos43 = 1
    elif state[1,3] < state[4,3]:
        pos13= 1
        pos43 = -1
    else:
        pos13 = 0
        pos43 = 0

    if state[1,6] > state[4,0]:
        pos16 = -1
        pos40 = 1
    elif state[1,6] < state[4,0]:
        pos16 = 1
        pos40 = -1
    else:
        pos16 = 0
        pos40 = 0

    action = np.array([[pos00, 0, 0, 0, 0, 0, 0, 0, 0], [pos10, 0, 0, pos13, 0, 0, pos16, 0, 0], [pos20, 0, pos22, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [pos40, 0, 0, pos43, 0, 0, pos46, 0, 0], [pos50, 0, 0, 0, 0, 0, 0, 0, 0]])
    return state + action

def move_mv(state):

    if state[0,1] > state[5,1]:
        pos01 = -1
        pos51 = 1
    elif state[0,1] < state[5,1]:
        pos01 = 1
        pos51 = -1
    else:
        pos01 = 0
        pos51 = 0
        
    if state[1,1] > state[4,7]:
        pos11 = -1
        pos47 = 1
    elif state[1,1] < state[4,7]:
        pos11 = 1
        pos47 = -1
    else:
        pos11 = 0
        pos47 = 0

    if state[1,4] > state[4,4]:
        pos14 = -1
        pos44 = 1
    elif state[1,4] < state[4,4]:
        pos14 = 1
        pos44 = -1
    else:
        pos14 = 0
        pos44 = 0

    if state[1,7] > state[4,1]:
        pos17 = -1
        pos41 = 1
    elif state[1,7] < state[4,1]:
        pos17= 1
        pos41 = -1
    else:
        pos17 = 0
        pos41 = 0

    action = np.array([[0 ,pos01, 0, 0, 0, 0, 0, 0, 0], [0, pos11, 0, 0, pos14, 0, 0, pos17, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, pos41, 0, 0, pos44, 0, 0, pos47, 0], [0, pos51, 0, 0, 0, 0, 0, 0, 0]])
    return state + action

def move_rv(state):

    if state[0,2] > state[5,2]:
        pos02 = -1
        pos52 = 1
    elif state[0,2] < state[5,2]:
        pos02 = 1
        pos52 = -1
    else:
        pos02 = 0
        pos52 = 0

    if state[3,0] > state[3,2]:
        pos30 = -1
        pos32 = 1
    elif state[3,0] < state[3,2]:
        pos30 = 1
        pos32 = -1
    else:
        pos30 = 0
        pos32 = 0

    if state[1,2] > state[4,8]:
        pos12 = -1
        pos48 = 1
    elif state[1,2] < state[4,8]:
        pos12 = 1
        pos48 = -1
    else:
        pos12 = 0
        pos48 = 0

    if state[1,5] > state[4,5]:
        pos15 = -1
        pos45 = 1
    elif state[1,5] < state[4,5]:
        pos15= 1
        pos45 = -1
    else:
        pos15 = 0
        pos45 = 0

    if state[1,8] > state[4,2]:
        pos18 = -1
        pos42 = 1
    elif state[1,8] < state[4,2]:
        pos18 = 1
        pos42 = -1
    else:
        pos18 = 0
        pos42 = 0

    action = np.array([[0 ,0 ,pos02, 0, 0, 0, 0, 0, 0], [0, 0, pos12, 0, 0, pos15, 0, 0, pos18], [0, 0, 0, 0, 0, 0, 0, 0, 0], [pos30, 0, pos32, 0, 0, 0, 0, 0, 0], [0, 0, pos42, 0, 0, pos45, 0, 0, pos48], [0, 0, pos52, 0, 0, 0, 0, 0, 0]])
    return state + action

def move_uh(state):

    if state[2,0] > state[3,0]:
        pos20 = -1
        pos30 = 1
    elif state[2,0] < state[3,0]:
        pos20 = 1
        pos30 = -1
    else:
        pos20 = 0
        pos30 = 0

    if state[0,0] > state[0,2]:
        pos00 = -1
        pos02 = 1
    elif state[0,0] < state[0,2]:
        pos00 = 1
        pos02 = -1
    else:
        pos00 = 0
        pos02 = 0

    if state[1,0] > state[4,2]:
        pos10 = -1
        pos42 = 1
    elif state[1,0] < state[4,2]:
        pos10 = 1
        pos42 = -1
    else:
        pos10 = 0
        pos42 = 0

    if state[1,1] > state[4,1]:
        pos11 = -1
        pos41 = 1
    elif state[1,1] < state[4,1]:
        pos11 = 1
        pos41 = -1
    else:
        pos11 = 0
        pos41 = 0

    if state[1,2] > state[4,0]:
        pos12 = -1
        pos40 = 1
    elif state[1,2] < state[4,0]:
        pos12 = 1
        pos40 = -1
    else:
        pos12 = 0
        pos40 = 0

    action = np.array([[pos00 ,0 ,pos02, 0, 0, 0, 0, 0, 0], [pos10, pos11, pos12, 0, 0, 0, 0, 0, 0], [pos20, 0, 0, 0, 0, 0, 0, 0, 0], [pos30, 0, 0, 0, 0, 0, 0, 0, 0], [pos40, pos41, pos42, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0 ,0 ,0, 0]])
    return state + action

def move_mh(state):

    if state[2, 1] > state[3, 1]:
        pos21 = -1
        pos31 = 1
    elif state[2, 1] < state[3, 1]:
        pos21 = 1
        pos31 = -1
    else:
        pos21 = 0
        pos31 = 0

    if state[1, 3] > state[4, 5]:
        pos13 = -1
        pos45 = 1
    elif state[1, 3] < state[4, 5]:
        pos13 = 1
        pos45 = -1
    else:
        pos13 = 0
        pos45 = 0

    if state[1,4] > state[4,4]:
        pos14 = -1
        pos44 = 1
    elif state[1,4] < state[4,4]:
        pos14 = 1
        pos44 = -1
    else:
        pos14 = 0
        pos44 = 0

    if state[1,5] > state[4,3]:
        pos15 = -1
        pos43 = 1
    elif state[1,5] < state[4,3]:
        pos15= 1
        pos43 = -1
    else:
        pos15 = 0
        pos43 = 0

    action = np.array([[0 ,0 ,0, 0, 0, 0, 0, 0, 0], [0, 0, 0, pos13, pos14, pos15, 0, 0, 0], [0, pos21, 0, 0, 0, 0, 0, 0, 0], [0, pos31, 0, 0, 0, 0, 0 ,0 ,0], [0, 0, 0, pos43, pos44, pos45, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]])
    return state + action

def move_dh(state):

    if state[2,2] > state[3,2]:
        pos22 = -1
        pos32 = 1
    elif state[2,2] < state[3,2]:
        pos22 = 1
        pos32 = -1
    else:
        pos22 = 0
        pos32 = 0

    if state[5,0] > state[5,2]:
        pos50 = -1
        pos52 = 1
    elif state[5,0] < state[5,2]:
        pos50 = 1
        pos52 = -1
    else:
        pos50 = 0
        pos52 = 0

    if state[1,6] > state[4,8]:
        pos16 = -1
        pos48 = 1
    elif state[1,6] < state[4,8]:
        pos16= 1
        pos48= -1
    else:
        pos16= 0
        pos48= 0

    if state[1,7] > state[4,7]:
        pos17= -1
        pos47= 1
    elif state[1,7] < state[4,7]:
        pos17 = 1
        pos47 = -1
    else:
        pos17 = 0
        pos47 = 0

    if state[1,8] > state[4,6]:
        pos18 = -1
        pos46 = 1
    elif state[1,8] < state[4,6]:
        pos18 = 1
        pos46 = -1
    else:
        pos18 = 0
        pos46 = 0

    action = np.array([[0 ,0 ,0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, pos16, pos17, pos18], [0, 0, pos22, 0, 0, 0, 0, 0 ,0], [0, 0, pos32, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, pos46, pos47, pos48], [pos50, 0, pos52, 0, 0, 0, 0, 0, 0]])
    return state + action


actions_dict = {'move_vi': move_lv, 'move_vc': move_mv, 'move_vd': move_rv,
                'move_hs': move_uh, 'move_hc': move_mh, 
                'move_hd': move_dh}

# We should define a class problem.
# For this example we will use the missionaries and cannibals problem
class Problem:
  #--------------------------------
  def __init__(self, initial_state, goal_state, actions_dict):
    self.initial_state = initial_state
    self.goal_state = goal_state
    self.actions_dict = actions_dict
  
  # Given the state, we should return the available actions
  def actions(self, state):
    return list(actions_dict.keys())
  
  # It should return the resulting state of applying the action to the current state
  def results(self, state, action):
    r = self.actions_dict[action](state)
    
    # Validate result
    if np.any(r<0):
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
    s = s + solution(node.parent)
    return s

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
p = Problem(np.array([[1 ,1 ,1, 0, 0, 0, 0, 0, 0], [6, 6, 6, 5, 5, 5, 5, 5, 5], [4, 3, 3, 0, 0, 0, 0, 0, 0], [3, 4, 4, 0, 0, 0, 0, 0, 0], [5, 5, 5, 6, 6, 6, 6, 6, 6], [2, 2, 2, 0, 0, 0, 0, 0, 0]]), np.array([[1, 1, 1, 0, 0, 0, 0, 0, 0], [5, 5, 5, 5, 5, 5, 5, 5, 5], [3, 3, 3, 0, 0, 0, 0, 0, 0], [4, 4, 4, 0, 0, 0, 0, 0, 0], [6, 6, 6, 6, 6, 6, 6, 6, 6], [2, 2, 2, 0, 0, 0, 0, 0, 0]]), actions_dict)

# Search for solution
sol = dfs(p)

# Show solution
for s in sol[::-1]:
  print("{} -> {}".format(s.action, s.state))