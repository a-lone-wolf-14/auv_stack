import serial
import rclpy
from rclpy.node import Node
from auv_interfaces.msg import ThrusterCommand

class SerialThrusterDriver(Node):

    def __init__(self):
        super().__init__('serial_thruster_driver')

        self.declare_parameter('port', '/dev/ttyS4')
        self.declare_parameter('baud', 115200)

        port = self.get_parameter('port').value
        baud = self.get_parameter('baud').value

        self.ser = serial.Serial(port, baud, timeout=1)

        self.subscription = self.create_subscription(
            ThrusterCommand,
            '/thruster/pwm',
            self.send_pwm,
            10
        )

    def send_pwm(self, msg):
        cmd = f"{msg.FL}/{msg.FR}/{msg.BL}/{msg.BR}/" \
              f"{msg.SL}/{msg.SR}/{msg.SF}/{msg.SB}/" \
              f"{msg.flashlight}/{msg.gripper}/\n"

        self.ser.write(cmd.encode())

def main(args=None):
    rclpy.init(args=args)
    node = SerialThrusterDriver()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()