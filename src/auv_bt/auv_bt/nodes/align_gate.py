import py_trees
from auv_bt.blackboard import Blackboard


class AlignGate(py_trees.behaviour.Behaviour):

    def __init__(self):
        super().__init__("AlignGate")

    def update(self):

        if not Blackboard.gate_visible:
            return py_trees.common.Status.FAILURE

        error = Blackboard.gate_offset

        if abs(error) < 0.05:
            return py_trees.common.Status.SUCCESS

        # publish yaw correction command

        return py_trees.common.Status.RUNNING
