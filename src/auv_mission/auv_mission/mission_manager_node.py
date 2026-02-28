import rclpy
from rclpy.node import Node
import yaml

class MissionManager(Node):

    def __init__(self):

        super().__init__("mission_manager")

        with open("config/mission.yaml") as f:
            mission = yaml.safe_load(f)

        self.tasks = mission["mission"]["tasks"]

        self.get_logger().info(f"Mission Tasks: {self.tasks}")


def main():

    rclpy.init()

    node = MissionManager()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()
