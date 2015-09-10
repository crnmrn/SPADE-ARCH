__author__ = 'Curtis'

pe_index = 0;


class PE(object):
    """
    Data structure for storing PE dependency data
    """
    def __init__(self, operation, pe_inputs, pe_outputs):
        self.operation = operation
        self.pe_inputs = pe_inputs
        self.pe_outputs = pe_outputs


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


def create_dependency_list(pe_list, net_map):
    dep_list = list()
    for pe in pe_list:
        for pe_dep_candidate in pe_list:
            if any(pe_io in pe.pe_inputs for pe_io in pe_dep_candidate.outputs):
                for dep in dep_list:
                    if dep[-1] is pe_dep_candidate:
                        dep.append(pe)
                dep_list.append([pe_dep_candidate, pe])





    for pe_x in pe_list:
        for pe_y in pe_list:
            if pe_x is not pe_y:
                """Check if pe_x.input map to pe_y.output and vica versa"""
                for nets in net_map:
                    for pe_in in pe_x.input:
                        if pe_in in nets and pe_y.output in nets:
                            for dep_chain in dep_list:
                                if pe_y in dep_chain[0]:
                                    dep_chain.append(pe_x)
                                else:
                                    dep_list.append([pe_y, pe_x])
    return list()