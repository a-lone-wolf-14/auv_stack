from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    return LaunchDescription([
        Node(package='auv_perception',
             executable='yolo_front_node'),

        Node(package='auv_perception',
             executable='aruco_detector_node'),
    ])