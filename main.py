import json
import os.path

from cube import RubiksCube
from solver import IDA_star

def build_heuristic_db(state, actions, max_moves = 20, heuristic = None):
    if heuristic is None:
        heuristic = {state: 0}
    que = [(state, 0)]
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
    return heuristic

#--------------------------------

if os.path.exists('heuristic.json'):
    with open('heuristic.json') as f:
        h_db = json.load(f)
else:
    h_db = None

cube = RubiksCube(n=3)
cube.show()
print('-----------')

actions = [(r, n, d) for r in ['h', 'v', 's'] for d in [0, 1] for n in range(cube.n)]
h_db = build_heuristic_db(
    cube.stringify(),
    actions,
    max_moves = 20,
    heuristic = h_db
)

with open('heuristic.json', 'w', encoding='utf-8') as f:
    json.dump(
        h_db,
        f,
        ensure_ascii=False,
        indent=4
    )

#--------------------------------

cube.horizontal_twist(1, 0)
cube.vertical_twist(1, 0)
cube.side_twist(0, 1)
cube.horizontal_twist(0, 1)
#cube.horizontal_twist(1, 0)
#cube.vertical_twist(1, 0)
#cube.horizontal_twist(1, 0)
cube.show()
print('----------')
#--------------------------------

solver = IDA_star(h_db)
moves = solver.run(cube.stringify())
print(moves)

for m in moves:
    if m[0] == 'h':
        cube.horizontal_twist(m[1], m[2])
    elif m[0] == 'v':
        cube.vertical_twist(m[1], m[2])
    elif m[0] == 's':
        cube.side_twist(m[1], m[2])
cube.show()
