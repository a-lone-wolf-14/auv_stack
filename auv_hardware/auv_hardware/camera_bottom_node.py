import cv2
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

class BottomCameraNode(Node):

    def __init__(self):
        super().__init__('camera_bottom_node')

        self.cap = cv2.VideoCapture('/dev/video2')
        self.bridge = CvBridge()

        self.pub_raw = self.create_publisher(
            Image,
            '/camera/bottom/image_raw',
            10
        )

        self.timer = self.create_timer(1/30.0, self.publish_frame)

    def publish_frame(self):
        ret, frame = self.cap.read()
        if not ret:
            return

        msg = self.bridge.cv2_to_imgmsg(frame, 'bgr8')
        self.pub_raw.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = BottomCameraNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()