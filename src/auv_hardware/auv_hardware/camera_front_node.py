import cv2
import rclpy
from rclpy.node import Node

from sensor_msgs.msg import Image
from sensor_msgs.msg import CompressedImage

from cv_bridge import CvBridge


class FrontCameraNode(Node):

    def __init__(self):
        super().__init__('camera_front_node')

        self.cap = cv2.VideoCapture('/dev/video0')

        self.bridge = CvBridge()

        # RAW image publisher
        self.pub_raw = self.create_publisher(
            Image,
            '/camera/front/image_raw',
            10
        )

        # COMPRESSED image publisher
        self.pub_compressed = self.create_publisher(
            CompressedImage,
            '/camera/front/image_compressed',
            10
        )

        self.timer = self.create_timer(1/30.0, self.publish_frame)

    def publish_frame(self):

        ret, frame = self.cap.read()
        if not ret:
            return

        # ======================
        # Publish RAW image
        # ======================
        raw_msg = self.bridge.cv2_to_imgmsg(frame, encoding='bgr8')
        self.pub_raw.publish(raw_msg)

        # ======================
        # Publish COMPRESSED image
        # ======================
        ret, buffer = cv2.imencode('.jpg', frame)

        comp_msg = CompressedImage()
        comp_msg.format = "jpeg"
        comp_msg.data = buffer.tobytes()

        self.pub_compressed.publish(comp_msg)


def main(args=None):

    rclpy.init(args=args)

    node = FrontCameraNode()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()
