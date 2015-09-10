__author__ = 'Curtis'
"""
This is a simple staged scheduler that will mainly keep track of dependencies between operations.
It assumes that the setup is columns of PE cascaded by switches and that all PEs and Switches are
homogeneous.
"""


def schedule_spa(pe_list, dependency_map):
    """
    Organize dependency list into rows.
    if a row is maxed out, move to next row.
    place any necessary no-op buffers.

    edge cases:
    -
    :return:
    """
    columns = make_columns(pe_list, dependency_map)
    add_buffers()
    finalize_routes(columns)


def make_columns(pe_list, dependency_map):



def add_buffers(columns):
    for column in columns:
        """ Find a PE with an input not in the previous column. Go back and fill in no-ops until data dep is satisfied"""


def final_routes(columns):

