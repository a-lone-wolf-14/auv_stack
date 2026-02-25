from ultralytics import YOLO
import threading
import queue
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from auv_interfaces.msg import YoloDetection

class YoloNode(Node):

    def __init__(self):
        super().__init__('yolo_node')

        self.model = YOLO("best.pt")
        self.bridge = CvBridge()
        self.queue = queue.Queue(maxsize=1)

        self.pub_det = self.create_publisher(YoloDetection, "/yolo/detections", 10)
        self.pub_img = self.create_publisher(Image, "/yolo/image_annotated", 10)

        self.create_subscription(Image,
                                 "/camera/front/image_raw",
                                 self.callback,
                                 10)

        self.thread = threading.Thread(target=self.worker)
        self.thread.daemon = True
        self.thread.start()

    def callback(self, msg):
        frame = self.bridge.imgmsg_to_cv2(msg, "bgr8")
        if not self.queue.full():
            self.queue.put(frame)

    def worker(self):
        while rclpy.ok():
            try:
                frame = self.queue.get(timeout=0.5)
            except queue.Empty:
                continue

            results = self.model(frame, verbose=False)

            for box in results[0].boxes:
                det = YoloDetection()
                det.class_id = int(box.cls[0])
                det.confidence = float(box.conf[0])
                self.pub_det.publish(det)

            annotated = results[0].plot()
            img_msg = self.bridge.cv2_to_imgmsg(annotated, "bgr8")
            self.pub_img.publish(img_msg)

def main(args=None):
    rclpy.init(args=args)

    node = YoloNode()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()