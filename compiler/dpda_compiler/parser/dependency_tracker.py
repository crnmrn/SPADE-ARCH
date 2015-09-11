__author__ = 'Curtis Mackay'

pe_index = 0;
import itertools

class PE(object):
    """
    Data structure for storing PE dependency data
    """
    newid = itertools.count().__next__

    def __init__(self, operation, pe_inputs, pe_outputs, pe_id=None):
        self.operation = operation
        self.pe_inputs = pe_inputs
        self.pe_outputs = pe_outputs
        if pe_id is None:
            self.pe_id = PE.newid()
        else:
            self.pe_id = pe_id

    def __repr__(self):
        return "PE %s" % self.pe_id
        # return "PE inputs:%s, outputs:%s" % (self.pe_inputs, self.pe_outputs)

    def __str__(self):
        return "PE inputs:%s, outputs:%s" % (self.pe_inputs, self.pe_outputs)


def compress_mapping(pe_list, net_map):
    for pe in pe_list:
        for i in range(len(pe.pe_inputs)):
            for net_set in net_map:
                if pe.pe_inputs[i] in net_set:
                    pe.pe_inputs[i] = net_set[0]
        for i in range(len(pe.pe_outputs)):
            for net_set in net_map:
                if pe.pe_outputs[i] in net_set:
                    pe.pe_outputs[i] = net_set[0]


def create_dependency_list(pe_list):
    dep_list = list()
    for pe in pe_list:
        for pe_dep_candidate in pe_list:
            input_set = set(pe.pe_inputs)
            output_set = set(pe_dep_candidate.pe_outputs)
            if input_set & output_set:
                new_dependency = True
                for dep in dep_list:
                    if dep[-1] is pe_dep_candidate:
                        dep.append(pe)
                        new_dependency = False
                if new_dependency:
                    dep_list.append([pe_dep_candidate, pe])
    # Add in any PE's that have no dependency
    for pe in pe_list:
        # optimized way to flatten list
        flattened_dep_list = [item for sublist in dep_list for item in sublist]
        if pe not in set(flattened_dep_list):
            dep_list.append([pe])
    return dep_list