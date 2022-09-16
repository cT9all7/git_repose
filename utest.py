import unittest


import mouse_move

class test_mouse_move (unittest.TestCase):
    def test_mouse(self):
        self.assertEqual(mouse_move.mouse_move(),(1920,1080))

unittest.main()

