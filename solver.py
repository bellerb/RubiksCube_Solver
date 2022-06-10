from random import choice
from cube import RubiksCube

class IDA_star(object):
    def __init__(self, heuristic, colour = 'w', max_depth = 20):
        self.max_depth = max_depth
        self.colour = colour
        self.threshold = max_depth
        self.min_threshold = None
        self.heuristic = heuristic
        self.moves = []

    def run(self, state):
        while True:
            status = self.search(state, 1)
            if status: return self.moves
            self.moves = []
            self.threshold = self.min_threshold
        return []

    def search(self, state, g_score):
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
