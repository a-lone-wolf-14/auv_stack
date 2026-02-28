import py_trees


class DepthHold(py_trees.behaviour.Behaviour):

    def __init__(self):
        super().__init__("DepthHold")

    def update(self):

        # depth PID handled elsewhere
        return py_trees.common.Status.SUCCESS
