import unittest
from src.search.score import Mate, Eval, Score
import time

class TestScore(unittest.TestCase):
    """ A bunch of test cases to be certain that the Score module works
    the way it should. 

    We test white solo, black solo, and backpropagation to ensure that
    there are no bugs.
    """
    def test_white_score(self):
        ### mate-mate tests
        # white side equal
        self.assertEqual(Mate(0, True, True), Mate(0, True, True))
        self.assertEqual(Mate(1, True, True), Mate(1, True, True))
        self.assertEqual(Mate(1, False, True), Mate(1, False, True))

        # closer white side mate, implies further white side mate
        self.assertGreater(Mate(1, True, True), Mate(2, True, True))
        self.assertGreater(Mate(0, True, True), Mate(2, True, True))
        self.assertGreater(Mate(3, True, True), Mate(4, True, True))

        # always choose white mate over black mate
        self.assertGreater(Mate(500, True, True), Mate(0, False, True))
        self.assertGreater(Mate(0, True, True), Mate(0, False, True))
        self.assertGreater(Mate(500, True, True), Mate(500, False, True))

        ### eval-eval tests
        # white side equal
        self.assertEqual(Eval(0.0, turn=True), Eval(0.0, turn=True))
        self.assertEqual(Eval(-0.123456, turn=True), Eval(-0.123456, turn=True))
        self.assertNotEqual(Eval(0.123455, turn=True), Eval(0.123456, turn=True))

        # higher white score, better position, implies worse white score
        self.assertGreater(Eval(0.123, turn=True), Eval(0.122, turn=True))
        self.assertGreater(Eval(0.123, turn=True), Eval(-1, turn=True))
        self.assertGreater(Eval(-0.5, turn=True), Eval(-0.6, turn=True))

        ### eval-mate tests
        # always choose white mate over eval
        self.assertGreater(Mate(500, True, True), Eval(1000, True))
        self.assertGreater(Mate(0, True, True), Eval(1000, True))
        self.assertGreater(Mate(500, True, True), Eval(0, True))
        self.assertGreater(Mate(500, True, True), Eval(-1000, True))
        
        # always choose eval over black mate
        self.assertGreater(Eval(300, turn=True), Mate(0, False, True))
        self.assertGreater(Eval(-100, turn=True), Mate(0, False, True))
        self.assertGreater(Eval(-100, turn=True), Mate(500, False, True))
        self.assertGreater(Eval(0, turn=True), Mate(0, False, True))

    def test_black_score(self):
        ### mate-mate tests
        # black side equal
        self.assertEqual(Mate(0, False, False), Mate(0, False, False))
        self.assertEqual(Mate(1, False, False), Mate(1, False, False))
        self.assertEqual(Mate(1, True, False), Mate(1, True, False))

        # closer black side mate, implies further black side mate
        self.assertGreater(Mate(1, False, False), Mate(2, False, False))
        self.assertGreater(Mate(0, False, False), Mate(2, False, False))
        self.assertGreater(Mate(3, False, False), Mate(4, False, False))

        # always choose black mate over white
        self.assertLess(Mate(500, True, False), Mate(0, False, False))
        self.assertLess(Mate(0, True, False), Mate(0, False, False))
        self.assertLess(Mate(500, True, False), Mate(500, False, False))

        ### eval-eval tests
        # black side equal
        self.assertEqual(Eval(0.0, turn=False), Eval(0.0, turn=False))
        self.assertEqual(Eval(-0.123456, turn=False), Eval(-0.123456, turn=False))
        self.assertNotEqual(Eval(0.123455, turn=False), Eval(0.123456, turn=False))

        # higher black score, better position, implies worse black score
        self.assertGreater(Eval(-0.123, turn=False), Eval(-0.122, turn=False))
        self.assertGreater(Eval(-0.1, turn=False), Eval(0, turn=False))
        self.assertGreater(Eval(-0.1, turn=False), Eval(0.1, turn=False))
        self.assertGreater(Eval(0.5, turn=False), Eval(0.51, turn=False))

        ### eval-mate tests
        # always choose black mate over eval
        self.assertGreater(Mate(500, False, False), Eval(-100000, False))
        self.assertGreater(Mate(0, False, False), Eval(-1000, False))
        self.assertGreater(Mate(500, False, False), Eval(-1000, False))
        self.assertGreater(Mate(500, False, False), Eval(1000, False))
        
        # always choose eval over white mate
        self.assertGreater(Eval(-10000, turn=False), Mate(100, True, False))
        self.assertGreater(Eval(10000, turn=False), Mate(100, True, False))
        self.assertGreater(Eval(10000, turn=False), Mate(0, True, False))
        self.assertGreater(Eval(0, turn=False), Mate(0, True, False))

    def test_score_comparison_speed(self):
        num_it = 1_000_000
        score1, score2 = Eval(0.5, turn=False), Eval(0.4, turn=False)

        start = time.time()
        for i in range(num_it):
            x = score1 < score2
        end = time.time()
        elapsed = end - start
        print(f"{round(num_it/elapsed, 3)} it/s: ", end= "status = ", flush=True)

    def test_eval_backpropagation(self):
        # check backpropagation
        score : Eval = Eval(0.5, True)
        scoreNext : Eval = score.get_propagated_score()

        self.assertNotEqual(score.turn, scoreNext.turn)
        self.assertEqual(score.evaluation, scoreNext.evaluation)

        self.assertEqual(score, scoreNext.get_propagated_score())

        # check values are not linked
        score : Eval = Eval(0.5, True)
        scoreNext : Eval = score.get_propagated_score()
        scoreNext.turn = True
        self.assertEqual(score, scoreNext)
        scoreNext.evaluation = 0.4
        self.assertNotEqual(score, scoreNext)

    def test_mate_backpropagation(self):
        mate_in = 5
        score : Mate = Mate(mate_in, True, True)
        scoreNext : Mate = score.get_propagated_score()

        self.assertEqual(scoreNext.mate_in, mate_in + 1)
        self.assertEqual(score.mate_side, scoreNext.mate_side)
        self.assertNotEqual(score.turn, scoreNext.turn)

    def test_backpropagation_speed(self):
        num_it = 1_000_000
        eval = Eval(0.5, True)
        mate = Mate(0, True, True)

        start = time.time()
        for i in range(int(num_it / 2)):
            eval.get_propagated_score()
            mate.get_propagated_score()
        end = time.time()
        elapsed = end - start
        print(f"{round(num_it/elapsed, 3)} it/s: ", end= "status = ", flush=True)



if __name__ == '__main__':
    ## run using: python score_test.py -v

    # clear
    import os
    os.system("clear")
    print("##### Commencing Test:")

    # start
    unittest.main()