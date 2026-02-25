import cv2
import numpy as np
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from auv_interfaces.msg import AruCoDetection

class ArucoDetector(Node):

    def __init__(self):
        super().__init__('aruco_detector')

        self.bridge = CvBridge()
        self.dict = cv2.aruco.getPredefinedDictionary(
            cv2.aruco.DICT_4X4_50)

        self.detector = cv2.aruco.ArucoDetector(self.dict)

        self.sub = self.create_subscription(
            Image,
            '/camera/bottom/image_raw',
            self.callback,
            10
        )

        self.pub = self.create_publisher(
            AruCoDetection,
            '/aruco/detections',
            10
        )

    def callback(self, msg):
        frame = self.bridge.imgmsg_to_cv2(msg, 'bgr8')
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        corners, ids, _ = self.detector.detectMarkers(gray)

        if ids is None:
            return

        for i, marker_id in enumerate(ids):
            det = AruCoDetection()
            det.marker_id = int(marker_id[0])
            self.pub.publish(det)

def main(args=None):
    rclpy.init(args=args)
    node = ArucoDetector()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()