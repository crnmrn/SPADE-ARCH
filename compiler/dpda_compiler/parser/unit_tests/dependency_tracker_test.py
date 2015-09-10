__author__ = 'Curtis'

import unittest
import dpda_compiler.parser.dependency_tracker as dep

pe_list = [dep.PE('mult', ['a', 'b'], ['u']),
           dep.PE('mult', ['c', 'd'], ['v']),
           dep.PE('mult', ['e', 'f'], ['w']),
           dep.PE('mult', ['g', 'h'], ['x']),
           dep.PE('mult', ['i', 'j'], ['y']),
           dep.PE('mult', ['k', 'l'], ['z'])]

net_map = [('u', 'm', 'e'), ('v', 'k'), ('w', 'h'), ('x', 'n', 'i'), ('o', 'f')]


class DependencyTests(unittest.TestCase):
    def test_make_dependency_list(self):
        dep_list = dep.create_dependency_list(pe_list, net_map)
        self.assertIsInstance(dep_list, list)

    def test_check_valid_dependency_list(self):
        dep_list = dep.create_dependency_list(pe_list, net_map)
        self.assertGreater(len(dep_list), 0)
        for pe_dep in dep_list:
            self.assertIsInstance(pe_dep, list)
            self.assertGreaterEqual(len(pe_dep), 1)

    def test_compress_mapping(self):
        dep.compress_mapping(pe_list, net_map)
        self.assertIs('u', pe_list[0].pe_outputs[0])
        self.assertIs('c', pe_list[1].pe_inputs[0])
        self.assertIs('u', pe_list[2].pe_inputs[0])
        self.assertIs('o', pe_list[2].pe_inputs[1])
        self.assertIs('w', pe_list[3].pe_inputs[1])
        self.assertIs('x', pe_list[4].pe_inputs[0])
        self.assertIs('v', pe_list[5].pe_inputs[0])


if __name__ == '__main__':
    unittest.main()
