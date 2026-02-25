import rclpy
from rclpy.node import Node
from auv_interfaces.msg import ThrusterCommand

class ThrusterMixer(Node):

    def __init__(self):
        super().__init__('thruster_mixer')

        self.sub = self.create_subscription(
            ThrusterCommand,
            "/control/forces",
            self.mix,
            10
        )

        self.pub = self.create_publisher(
            ThrusterCommand,
            "/thruster/pwm",
            10
        )

    def mix(self, msg):
        X = msg.sl
        Y = msg.sf
        Z = msg.fl
        Yaw = msg.fr
        Pitch = msg.bl
        Roll = msg.br

        fl = Z - Roll - Pitch
        fr = Z + Roll - Pitch
        bl = Z - Roll + Pitch
        br = Z + Roll + Pitch

        sl = X
        sr = X

        sf = Y + Yaw
        sb = Y - Yaw

        out = ThrusterCommand()
        out.fl = fl
        out.fr = fr
        out.bl = bl
        out.br = br
        out.sl = sl
        out.sr = sr
        out.sf = sf
        out.sb = sb
        out.flashlight = 1
        out.gripper = 0

        self.pub.publish(out)