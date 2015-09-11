__author__ = 'Curtis'

import unittest
import dpda_compiler.parser.dependency_tracker as dep

pe_list = [dep.PE('mult', ['a', 'b'], ['u'], 0),
           dep.PE('mult', ['c', 'd'], ['v'], 1),
           dep.PE('mult', ['e', 'f'], ['w'], 2),
           dep.PE('mult', ['g', 'h'], ['x'], 3),
           dep.PE('mult', ['i', 'j'], ['y'], 4),
           dep.PE('mult', ['k', 'l'], ['z'], 5),
           dep.PE('mult', ['q', 'r'], ['o'], 6),
           dep.PE('mult', ['1', '2'], ['3'], 7)]

net_map = [('u', 'm', 'e'), ('v', 'k'), ('w', 'h'), ('x', 'n', 'i'), ('o', 'f')]

dep_list_expect = [[pe_list[0], pe_list[2], pe_list[3], pe_list[4]],
                   [pe_list[1], pe_list[5]],
                   [pe_list[6], pe_list[2], pe_list[3], pe_list[4]],
                   [pe_list[7]]]

class DependencyTests(unittest.TestCase):
    def test_make_dependency_list(self):
        dep_list = dep.create_dependency_list(pe_list)
        self.assertIsInstance(dep_list, list)

    def test_check_valid_dependency_list(self):
        dep.compress_mapping(pe_list, net_map)
        dep_list = dep.create_dependency_list(pe_list)
        self.assertGreater(len(dep_list), 0)
        for dep_item in dep_list_expect:
            self.assertIn(dep_item, dep_list, "%s not in dependency list" % dep_item)

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
