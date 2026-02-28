import py_trees
import time
from auv_bt.blackboard import Blackboard


class PassGate(py_trees.behaviour.Behaviour):

    def __init__(self):

        super().__init__("PassGate")

        self.start_time = None

    def update(self):

        if not Blackboard.gate_visible:
            return py_trees.common.Status.FAILURE

        if self.start_time is None:
            self.start_time = time.time()

        if time.time() - self.start_time > 4.0:
            return py_trees.common.Status.SUCCESS

        # publish forward command

        return py_trees.common.Status.RUNNING
