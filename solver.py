from random import choice
from tqdm import tqdm

from cube import RubiksCube

class IDA_star(object):
    def __init__(self, heuristic, max_depth = 20):
        """
        Input: heuristic - dictionary representing the heuristic pre computed map
               max_depth - integer representing the max depth you want your game tree to reach (default = 20) [OPTIONAL]
        Description: Initialize the solver
        Output: None
        """
        self.max_depth = max_depth
        self.threshold = max_depth
        self.min_threshold = None
        self.heuristic = heuristic
        self.moves = []

    def run(self, state):
        """
        Input: state - string representing the current state of the cube
        Description: solve the rubix cube
        Output: list containing the moves taken to solve the cube
        """
        while True:
            status = self.search(state, 1)
            if status: return self.moves
            self.moves = []
            self.threshold = self.min_threshold
        return []

    def search(self, state, g_score):
        """
        Input: state - string representing the current state of the cube
               g_score - integer representing the cost to reach the current node
        Description: search the game tree using the IDA* algorithm
        Output: boolean representing if the cube has been solved
        """
        cube = RubiksCube(state=state)
        if cube.solved():
            return True
        elif len(self.moves) >= self.threshold:
            return False
        min_val = float('inf')
        best_action = None
        for a in [(r, n, d) for r in ['h', 'v', 's'] for d in [0, 1] for n in range(cube.n)]:
            cube = RubiksCube(state=state)
            if a[0] == 'h':
                cube.horizontal_twist(a[1], a[2])
            elif a[0] == 'v':
                cube.vertical_twist(a[1], a[2])
            elif a[0] == 's':
                cube.side_twist(a[1], a[2])
            if cube.solved():
                self.moves.append(a)
                return True
            cube_str = cube.stringify()
            h_score = self.heuristic[cube_str] if cube_str in self.heuristic else self.max_depth
            f_score = g_score + h_score
            if f_score < min_val:
                min_val = f_score
                best_action = [(cube_str, a)]
            elif f_score == min_val:
                if best_action is None:
                    best_action = [(cube_str, a)]
                else:
                    best_action.append((cube_str, a))
        if best_action is not None:
            if self.min_threshold is None or min_val < self.min_threshold:
                self.min_threshold = min_val
            next_action = choice(best_action)
            self.moves.append(next_action[1])
            status = self.search(next_action[0], g_score + min_val)
            if status: return status
        return False

def build_heuristic_db(state, actions, max_moves = 20, heuristic = None):
    """
    Input: state - string representing the current state of the cube
           actions -list containing tuples representing the possible actions that can be taken
           max_moves - integer representing the max amount of moves alowed (default = 20) [OPTIONAL]
           heuristic - dictionary containing current heuristic map (default = None) [OPTIONAL]
    Description: create a heuristic map for determining the best path for solving a rubiks cube
    Output: dictionary containing the heuristic map
    """
    if heuristic is None:
        heuristic = {state: 0}
    que = [(state, 0)]
    node_count = sum([len(actions) ** (x + 1) for x in range(max_moves + 1)])
    with tqdm(total=node_count, desc='Heuristic DB') as pbar:
        while True:
            if not que:
                break
            s, d = que.pop()
            if d > max_moves:
                continue
            for a in actions:
                cube = RubiksCube(state=s)
                if a[0] == 'h':
                    cube.horizontal_twist(a[1], a[2])
                elif a[0] == 'v':
                    cube.vertical_twist(a[1], a[2])
                elif a[0] == 's':
                    cube.side_twist(a[1], a[2])
                a_str = cube.stringify()
                if a_str not in heuristic or heuristic[a_str] > d + 1:
                    heuristic[a_str] = d + 1
                que.append((a_str, d+1))
                pbar.update(1)
    return heuristic
