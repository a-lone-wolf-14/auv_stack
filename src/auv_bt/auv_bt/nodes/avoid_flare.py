import py_trees
from auv_bt.blackboard import Blackboard


class AvoidFlare(py_trees.behaviour.Behaviour):

    def __init__(self):
        super().__init__("AvoidFlare")

    def update(self):

        if not Blackboard.flare_visible:
            return py_trees.common.Status.FAILURE

        # publish avoidance command

        return py_trees.common.Status.RUNNING
