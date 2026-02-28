import py_trees


class CollideFlare(py_trees.behaviour.Behaviour):

    def __init__(self):
        super().__init__("CollideFlare")

    def update(self):

        # forward thrust

        return py_trees.common.Status.RUNNING
