import unittest

from cube import RubiksCube

class TestCube(unittest.TestCase):
    def test_cube_init(self):
        """
        Input: None
        Description: test to make sure the cube initializes properly
        Output: None
        """
        cube = RubiksCube(state='wwwwooooggggrrrrbbbbyyyy')
        self.assertEqual(
            [
                [
                    ['w', 'w'],
                    ['w', 'w']
                ],
                [
                    ['o', 'o'],
                    ['o', 'o']
                ],
                [
                    ['g', 'g'],
                    ['g', 'g']
                ],
                [
                    ['r', 'r'],
                    ['r', 'r']
                ],
                [
                    ['b', 'b'],
                    ['b', 'b']
                ],
                [
                    ['y', 'y'],
                    ['y', 'y']
                ]
            ], cube.cube)
        cube = RubiksCube(n = 2)
        self.assertEqual(
            [
                [
                    ['w', 'w'],
                    ['w', 'w']
                ],
                [
                    ['o', 'o'],
                    ['o', 'o']
                ],
                [
                    ['g', 'g'],
                    ['g', 'g']
                ],
                [
                    ['r', 'r'],
                    ['r', 'r']
                ],
                [
                    ['b', 'b'],
                    ['b', 'b']
                ],
                [
                    ['y', 'y'],
                    ['y', 'y']
                ]
            ], cube.cube)

    def test_horizontal(self):
        """
        Input: None
        Description: test to make sure horizontal rotations of cube are working
        Output: None
        """
        cube = RubiksCube(n=2)
        cube.horizontal_twist(1, 0) #Down or D'
        self.assertEqual(
            [
                [
                    ['w', 'w'],
                    ['w', 'w']
                ],
                [
                    ['o', 'o'],
                    ['g', 'g']
                ],
                [
                    ['g', 'g'],
                    ['r', 'r']
                ],
                [
                    ['r', 'r'],
                    ['b', 'b']
                ],
                [
                    ['b', 'b'],
                    ['o', 'o']
                ],
                [
                    ['y', 'y'],
                    ['y', 'y']
                ]
            ], cube.cube)
        cube.horizontal_twist(1, 1) #Up or D
        self.assertEqual(
            [
                [
                    ['w', 'w'],
                    ['w', 'w']
                ],
                [
                    ['o', 'o'],
                    ['o', 'o']
                ],
                [
                    ['g', 'g'],
                    ['g', 'g']
                ],
                [
                    ['r', 'r'],
                    ['r', 'r']
                ],
                [
                    ['b', 'b'],
                    ['b', 'b']
                ],
                [
                    ['y', 'y'],
                    ['y', 'y']
                ]
            ], cube.cube)
        cube.horizontal_twist(0, 0) #Down or U
        self.assertEqual(
            [
                [
                    ['w', 'w'],
                    ['w', 'w']
                ],
                [
                    ['g', 'g'],
                    ['o', 'o']
                ],
                [
                    ['r', 'r'],
                    ['g', 'g']
                ],
                [
                    ['b', 'b'],
                    ['r', 'r']
                ],
                [
                    ['o', 'o'],
                    ['b', 'b']
                ],
                [
                    ['y', 'y'],
                    ['y', 'y']
                ]
            ], cube.cube)
        cube.horizontal_twist(0, 1) #Up or U'
        self.assertEqual(
            [
                [
                    ['w', 'w'],
                    ['w', 'w']
                ],
                [
                    ['o', 'o'],
                    ['o', 'o']
                ],
                [
                    ['g', 'g'],
                    ['g', 'g']
                ],
                [
                    ['r', 'r'],
                    ['r', 'r']
                ],
                [
                    ['b', 'b'],
                    ['b', 'b']
                ],
                [
                    ['y', 'y'],
                    ['y', 'y']
                ]
            ], cube.cube)

    def test_vertical(self):
        """
        Input: None
        Description: test to make sure vertical rotations of cube are working
        Output: None
        """
        cube = RubiksCube(n=2)
        cube.vertical_twist(1, 0) #Down or R'
        self.assertEqual(
            [
                [
                    ['w', 'b'],
                    ['w', 'b']
                ],
                [
                    ['o', 'o'],
                    ['o', 'o']
                ],
                [
                    ['g', 'w'],
                    ['g', 'w']
                ],
                [
                    ['r', 'r'],
                    ['r', 'r']
                ],
                [
                    ['y', 'b'],
                    ['y', 'b']
                ],
                [
                    ['y', 'g'],
                    ['y', 'g']
                ]
            ], cube.cube)
        cube.vertical_twist(1, 1) #Up or R
        self.assertEqual(
            [
                [
                    ['w', 'w'],
                    ['w', 'w']
                ],
                [
                    ['o', 'o'],
                    ['o', 'o']
                ],
                [
                    ['g', 'g'],
                    ['g', 'g']
                ],
                [
                    ['r', 'r'],
                    ['r', 'r']
                ],
                [
                    ['b', 'b'],
                    ['b', 'b']
                ],
                [
                    ['y', 'y'],
                    ['y', 'y']
                ]
            ], cube.cube)
        cube.vertical_twist(0, 0) #Down or L
        self.assertEqual(
            [
                [
                    ['b', 'w'],
                    ['b', 'w']
                ],
                [
                    ['o', 'o'],
                    ['o', 'o']
                ],
                [
                    ['w', 'g'],
                    ['w', 'g']
                ],
                [
                    ['r', 'r'],
                    ['r', 'r']
                ],
                [
                    ['b', 'y'],
                    ['b', 'y']
                ],
                [
                    ['g', 'y'],
                    ['g', 'y']
                ]
            ], cube.cube)
        cube.vertical_twist(0, 1) #Up or L'
        self.assertEqual(
            [
                [
                    ['w', 'w'],
                    ['w', 'w']
                ],
                [
                    ['o', 'o'],
                    ['o', 'o']
                ],
                [
                    ['g', 'g'],
                    ['g', 'g']
                ],
                [
                    ['r', 'r'],
                    ['r', 'r']
                ],
                [
                    ['b', 'b'],
                    ['b', 'b']
                ],
                [
                    ['y', 'y'],
                    ['y', 'y']
                ]
            ], cube.cube)

    def test_side(self):
        """
        Input: None
        Description: test to make sure side rotations of cube are working
        Output: None
        """
        cube = RubiksCube(n=2)
        cube.side_twist(1, 0) #Down or F'
        self.assertEqual(
            [
                [
                    ['w', 'w'],
                    ['r', 'r']
                ],
                [
                    ['o', 'w'],
                    ['o', 'w']
                ],
                [
                    ['g', 'g'],
                    ['g', 'g']
                ],
                [
                    ['y', 'r'],
                    ['y', 'r']
                ],
                [
                    ['b', 'b'],
                    ['b', 'b']
                ],
                [
                    ['o', 'o'],
                    ['y', 'y']
                ]
            ], cube.cube)
        cube.side_twist(1, 1) #Up or F
        self.assertEqual(
            [
                [
                    ['w', 'w'],
                    ['w', 'w']
                ],
                [
                    ['o', 'o'],
                    ['o', 'o']
                ],
                [
                    ['g', 'g'],
                    ['g', 'g']
                ],
                [
                    ['r', 'r'],
                    ['r', 'r']
                ],
                [
                    ['b', 'b'],
                    ['b', 'b']
                ],
                [
                    ['y', 'y'],
                    ['y', 'y']
                ]
            ], cube.cube)
        cube.side_twist(0, 0) #Down or B
        self.assertEqual(
            [
                [
                    ['r', 'r'],
                    ['w', 'w']
                ],
                [
                    ['w', 'o'],
                    ['w', 'o']
                ],
                [
                    ['g', 'g'],
                    ['g', 'g']
                ],
                [
                    ['r', 'y'],
                    ['r', 'y']
                ],
                [
                    ['b', 'b'],
                    ['b', 'b']
                ],
                [
                    ['y', 'y'],
                    ['o', 'o']
                ]
            ], cube.cube)
        cube.side_twist(0, 1) #Up or B'
        self.assertEqual(
            [
                [
                    ['w', 'w'],
                    ['w', 'w']
                ],
                [
                    ['o', 'o'],
                    ['o', 'o']
                ],
                [
                    ['g', 'g'],
                    ['g', 'g']
                ],
                [
                    ['r', 'r'],
                    ['r', 'r']
                ],
                [
                    ['b', 'b'],
                    ['b', 'b']
                ],
                [
                    ['y', 'y'],
                    ['y', 'y']
                ]
            ], cube.cube)

    def test_multi_rotate(self):
        """
        Input: None
        Description: test to make sure multiple rotations of cube are working
        Output: None
        """
        cube = RubiksCube(n=2)
        cube.horizontal_twist(1, 0)
        cube.vertical_twist(1, 0)
        cube.side_twist(0, 1)
        cube.horizontal_twist(0, 1)
        self.assertEqual(
            [
                [
                    ['o', 'b'],
                    ['g', 'w']
                ],
                [
                    ['b', 'o'],
                    ['r', 'g']
                ],
                [
                    ['y', 'o'],
                    ['r', 'w']
                ],
                [
                    ['g', 'w'],
                    ['r', 'o']
                ],
                [
                    ['r', 'w'],
                    ['y', 'y']
                ],
                [
                    ['y', 'g'],
                    ['b', 'b']
                ]
            ], cube.cube)
        cube.horizontal_twist(0, 0)
        cube.side_twist(0, 0)
        cube.vertical_twist(1, 1)
        cube.horizontal_twist(1, 1)
        self.assertEqual(
            [
                [
                    ['w', 'w'],
                    ['w', 'w']
                ],
                [
                    ['o', 'o'],
                    ['o', 'o']
                ],
                [
                    ['g', 'g'],
                    ['g', 'g']
                ],
                [
                    ['r', 'r'],
                    ['r', 'r']
                ],
                [
                    ['b', 'b'],
                    ['b', 'b']
                ],
                [
                    ['y', 'y'],
                    ['y', 'y']
                ]
            ], cube.cube)


if __name__ == '__main__':
    unittest.main()
