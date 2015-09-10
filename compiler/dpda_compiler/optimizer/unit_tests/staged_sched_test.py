__author__ = 'Curtis'

import unittest
import dpda_compiler.optimizer
import dpda_compiler.parser.dependency_tracker as dep

pe_list = [dep.DpdaOperation('mult', ['a', 'b'], 'u'),
           dep.DpdaOperation('mult', ['c', 'd'], 'v'),
           dep.DpdaOperation('mult', ['u', 'v'], 'w'),
           dep.DpdaOperation('mult', ['e', 'f'], 'x'),
           dep.DpdaOperation('mult', ['w', 'g'], 'y'),
           dep.DpdaOperation('mult', ['y', 'x'], 'z')]


class StageSchedulerTests(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
