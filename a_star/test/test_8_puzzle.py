from math import floor
import unittest

from puzzle import Puzzle
from state import State


class Test8Puzzle(unittest.TestCase):
    def setUp(self):
        self.puzzle = Puzzle(i=3, j=3)

    def tearDown(self):
        del self.puzzle


    def test_default_state(self):
        for i in range(3):
            for j in range(3):
                self.assertEqual(self.puzzle.tile_at(i, j), i * 3 + j)


    def test_setting_state(self):
        state = [8, 7, 6, 5, 4, 3, 2, 1, 0]
        puzzle = Puzzle(i=3, j=3, state=state)

        for i in reversed(range(3)):
            for j in reversed(range(3)):
                self.assertEqual(puzzle.tile_at(i, j), state[i * 3 + j])


    def test_tile_at(self):
        for i in range(3):
            for j in range(3):
                self.assertEqual(self.puzzle.tile_at(i, j), i * 3 + j)

    def test_all_movements(self):
        self.puzzle.move(Puzzle.RIGHT)
        self.puzzle.move(Puzzle.DOWN)
        self.puzzle.move(Puzzle.LEFT)
        self.puzzle.move(Puzzle.UP)

        self.assertEqual(self.puzzle.tile_at(0, 0), 0)
        self.assertEqual(self.puzzle.tile_at(0, 1), 4)
        self.assertEqual(self.puzzle.tile_at(0, 2), 2)
        self.assertEqual(self.puzzle.tile_at(1, 0), 1)
        self.assertEqual(self.puzzle.tile_at(1, 1), 3)
        self.assertEqual(self.puzzle.tile_at(1, 2), 5)
        self.assertEqual(self.puzzle.tile_at(2, 0), 6)
        self.assertEqual(self.puzzle.tile_at(2, 1), 7)
        self.assertEqual(self.puzzle.tile_at(2, 2), 8)

    def test_invalid_movements(self):
        self.puzzle.move(Puzzle.UP)
        self.assertEqual(self.puzzle.tile_at(0, 0), 0)

        self.puzzle.move(Puzzle.LEFT)
        self.assertEqual(self.puzzle.tile_at(0, 0), 0)

        self.puzzle.move(Puzzle.RIGHT)
        self.puzzle.move(Puzzle.RIGHT)
        self.puzzle.move(Puzzle.RIGHT)
        self.assertEqual(self.puzzle.tile_at(0, 2), 0)

        self.puzzle.move(Puzzle.DOWN)
        self.puzzle.move(Puzzle.DOWN)
        self.puzzle.move(Puzzle.DOWN)
        self.assertEqual(self.puzzle.tile_at(2, 2), 0)

    def test_equality_operator_overloading(self):
        self.assertTrue(
            Puzzle(i=3, j=3) == Puzzle(i=3, j=3)
        )

    def test_can_move_left(self):
        self.assertFalse(self.puzzle.can_move(Puzzle.LEFT))

        self.puzzle.move(Puzzle.RIGHT)

        self.assertTrue(self.puzzle.can_move(Puzzle.LEFT))

    def test_can_move_right(self):
        self.assertTrue(self.puzzle.can_move(Puzzle.RIGHT))

        self.puzzle.move(Puzzle.RIGHT)
        self.puzzle.move(Puzzle.RIGHT)

        self.assertFalse(self.puzzle.can_move(Puzzle.RIGHT))

    def test_can_move_down(self):
        self.assertTrue(self.puzzle.can_move(Puzzle.DOWN))

        self.puzzle.move(Puzzle.DOWN)
        self.puzzle.move(Puzzle.DOWN)

        self.assertFalse(self.puzzle.can_move(Puzzle.DOWN))

    def test_can_move_up(self):
        self.assertFalse(self.puzzle.can_move(Puzzle.UP))

        self.puzzle.move(Puzzle.DOWN)

        self.assertTrue(self.puzzle.can_move(Puzzle.UP))

    def test_puzzle_blank_position_updates(self):
        self.puzzle.move(Puzzle.DOWN)
        self.assertEqual(self.puzzle.blank_pos, 3)

        self.puzzle.move(Puzzle.UP)
        self.assertEqual(self.puzzle.blank_pos, 0)

        self.puzzle.move(Puzzle.RIGHT)
        self.assertEqual(self.puzzle.blank_pos, 1)

        self.puzzle.move(Puzzle.LEFT)
        self.assertEqual(self.puzzle.blank_pos, 0)

    def test_get_num_cols(self):
        self.assertEqual(self.puzzle.num_cols, 3)

    def test_num_rows(self):
        self.assertEqual(self.puzzle.num_rows, 3)

    def test_update_signature(self):
        self.puzzle.update_signature()
        self.assertEqual(self.puzzle.signature, 0x012345678)

    def test_update_signature_for_15_puzzle(self):
        puzzle = Puzzle(i=4, j=4)
        puzzle.update_signature()

        self.assertEqual(puzzle.signature, 0x0123456789abcdef)


    def test_updates_after_move(self):
        self.puzzle.move(self.puzzle.RIGHT)
        self.assertEqual(self.puzzle.signature, 4331951736)

    def test_hash(self):
        self.assertEqual(self.puzzle.__hash__(), 305419896)

