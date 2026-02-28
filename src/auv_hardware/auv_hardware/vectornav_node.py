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
        ang_vel = Registers.IMU.Gyro()
        lin_accel = Registers.IMU.Accel()
        self.sensor.readRegister(ypr)
        self.sensor.readRegister(ang_vel)
        self.sensor.readRegister(lin_accel)

        msg = Imu()
        msg.orientation.z = ypr.yaw
        msg.orientation.y = ypr.pitch
        msg.orientation.x = ypr.roll
        msg.angular_velocity.x = ang_vel.gyroX
        msg.angular_velocity.y = ang_vel.gyroY
        msg.angular_velocity.z = ang_vel.gyroZ
        msg.linear_acceleration.x = lin_accel.accelX
        msg.linear_acceleration.y = lin_accel.accelY
        msg.linear_acceleration.z = lin_accel.accelZ

        self.pub.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = VectorNavNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
