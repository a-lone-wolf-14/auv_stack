import py_trees
from auv_bt.blackboard import Blackboard


class SearchGate(py_trees.behaviour.Behaviour):

    def __init__(self):
        super().__init__("SearchGate")

    def update(self):

        if Blackboard.gate_visible:
            return py_trees.common.Status.FAILURE

        # command yaw search here

        return py_trees.common.Status.RUNNING
