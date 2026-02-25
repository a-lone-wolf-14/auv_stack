import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Imu
from vectornav import Sensor, Registers

class VectorNavNode(Node):
    def __init__(self):
        super().__init__('vectornav_node')

        self.sensor = Sensor()
        self.sensor.connect("/dev/ttyUSB0", 115200)

        self.pub = self.create_publisher(Imu, "/imu/data", 10)
        self.timer = self.create_timer(0.02, self.read_imu)

    def read_imu(self):
        ypr = Registers.Attitude.YawPitchRoll()
        self.sensor.readRegister(ypr)

        msg = Imu()
        msg.orientation.z = ypr.yaw
        msg.orientation.y = ypr.pitch
        msg.orientation.x = ypr.roll

        self.pub.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = Bar30Node()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()