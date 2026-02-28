import py_trees


class DockPoolbed(py_trees.behaviour.Behaviour):

    def __init__(self):
        super().__init__("DockPoolbed")

    def update(self):

        # descend and dock

        return py_trees.common.Status.RUNNING
