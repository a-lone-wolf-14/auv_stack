import py_trees
from auv_bt.blackboard import Blackboard


class ScanAruco(py_trees.behaviour.Behaviour):

    def __init__(self):
        super().__init__("ScanAruco")

    def update(self):

        if len(Blackboard.aruco_markers) >= 4:
            return py_trees.common.Status.SUCCESS

        return py_trees.common.Status.RUNNING
