import numpy as np
import rclpy
from rclpy.node import Node
from auv_interfaces.msg import StateEstimate
from sensor_msgs.msg import Imu, FluidPressure

class EKFNode(Node):

    def __init__(self):
        super().__init__('ekf_node')

        self.x = np.zeros((6,1))
        self.P = np.eye(6)
        self.Q = np.eye(6) * 0.01
        self.R = np.eye(6) * 0.1

        self.pub = self.create_publisher(StateEstimate, "/state/estimate", 10)

        self.create_subscription(Imu, "/imu/data", self.imu_cb, 10)
        self.create_subscription(FluidPressure, "/depth", self.depth_cb, 10)

    def imu_cb(self, msg):
        self.x[3] = msg.orientation.z
        self.x[4] = msg.orientation.y
        self.x[5] = msg.orientation.x

    def depth_cb(self, msg):
        self.x[2] = msg.fluid_pressure
        self.publish_state()

    def publish_state(self):
        msg = StateEstimate()
        msg.x = float(self.x[0])
        msg.y = float(self.x[1])
        msg.z = float(self.x[2])
        msg.yaw = float(self.x[3])
        msg.pitch = float(self.x[4])
        msg.roll = float(self.x[5])
        self.pub.publish(msg)

def main(args=None):
    rclpy.init(args=args)

    node = EKFNode()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()