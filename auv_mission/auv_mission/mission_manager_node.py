import rclpy
from rclpy.node import Node
from auv_interfaces.msg import YoloDetection, ThrusterCommand

class MissionManager(Node):

    def __init__(self):
        super().__init__('mission_manager')

        self.sub = self.create_subscription(
            YoloDetection,
            "/yolo/detections",
            self.yolo_cb,
            10
        )

        self.pub = self.create_publisher(
            ThrusterCommand,
            "/control/forces",
            10
        )

    def yolo_cb(self, msg):
        cmd = ThrusterCommand()
        cmd.sl = 0.3  # surge
        cmd.flashlight = 1
        cmd.gripper = 0
        self.pub.publish(cmd)

def main(args=None):
    rclpy.init(args=args)

    node = MissionManager()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()