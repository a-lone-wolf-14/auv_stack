import serial
import rclpy
from rclpy.node import Node

from sensor_msgs.msg import FluidPressure, Temperature
from std_msgs.msg import Int32


class Bar30Node(Node):
    def __init__(self):
        super().__init__('bar30_node')

        # Serial connection
        self.ser = serial.Serial("/dev/pts/2", 115200, timeout=1)

        # Publishers
        self.depth_pub = self.create_publisher(FluidPressure, "/depth", 10)
        self.pressure_pub = self.create_publisher(FluidPressure, "/pressure", 10)
        self.temp_pub = self.create_publisher(Temperature, "/temperature", 10)
        self.batt4s_pub = self.create_publisher(Int32, "/battery_4s", 10)
        self.batt5s_pub = self.create_publisher(Int32, "/battery_5s", 10)

        # Timer (20 Hz)
        self.timer = self.create_timer(0.05, self.read_data)

    def read_data(self):
        try:
            line = self.ser.readline().decode().strip()

            if not line:
                return

            data = line.split('/')

            if len(data) < 5:
                self.get_logger().warn(f"Incomplete data received: {line}")
                return

            # Parse values
            pressure = float(data[0])
            temperature = float(data[1])
            depth = float(data[2])
            batt_4s = int(data[3])
            batt_5s = int(data[4])

            # ---------------------------
            # Publish Depth
            # ---------------------------
            depth_msg = FluidPressure()
            depth_msg.fluid_pressure = depth
            self.depth_pub.publish(depth_msg)

            # ---------------------------
            # Publish Pressure
            # ---------------------------
            pressure_msg = FluidPressure()
            pressure_msg.fluid_pressure = pressure
            self.pressure_pub.publish(pressure_msg)

            # ---------------------------
            # Publish Temperature
            # ---------------------------
            temp_msg = Temperature()
            temp_msg.temperature = temperature
            self.temp_pub.publish(temp_msg)

            # ---------------------------
            # Publish Battery Voltages
            # ---------------------------
            batt4_msg = Int32()
            batt4_msg.data = batt_4s
            self.batt4s_pub.publish(batt4_msg)

            batt5_msg = Int32()
            batt5_msg.data = batt_5s
            self.batt5s_pub.publish(batt5_msg)

        except Exception as e:
            self.get_logger().error(f"Error parsing serial data: {e}")


def main(args=None):
    rclpy.init(args=args)
    node = Bar30Node()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
