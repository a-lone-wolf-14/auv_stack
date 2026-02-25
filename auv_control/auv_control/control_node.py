import rclpy
from rclpy.node import Node
from auv_interfaces.msg import StateEstimate, ThrusterCommand

class ControlNode(Node):

    def __init__(self):
        super().__init__('control_node')

        self.sub = self.create_subscription(
            StateEstimate,
            '/state/estimate',
            self.state_cb,
            10
        )

        self.pub = self.create_publisher(
            ThrusterCommand,
            '/control/forces',
            10
        )

    def state_cb(self, msg):
        cmd = ThrusterCommand()
        cmd.SL = 0.2  # simple surge test
        self.pub.publish(cmd)

def main(args=None):
    rclpy.init(args=args)
    node = ControlNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()