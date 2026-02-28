import rclpy
from rclpy.node import Node
import py_trees

from auv_bt.nodes.depth_hold import DepthHold
from auv_bt.nodes.search_gate import SearchGate
from auv_bt.nodes.align_gate import AlignGate
from auv_bt.nodes.pass_gate import PassGate


class BTRunner(Node):

    def __init__(self):

        super().__init__("bt_runner")

        root = py_trees.composites.Sequence("Mission")

        gate_selector = py_trees.composites.Selector("GateTask")

        pass_gate = PassGate()
        align_gate = AlignGate()
        search_gate = SearchGate()

        gate_selector.add_children([
            pass_gate,
            align_gate,
            search_gate
        ])

        root.add_children([
            DepthHold(),
            gate_selector
        ])

        self.tree = py_trees.trees.BehaviourTree(root)

        self.timer = self.create_timer(0.1, self.tick)

    def tick(self):
        self.tree.tick()


def main():

    rclpy.init()

    node = BTRunner()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()
