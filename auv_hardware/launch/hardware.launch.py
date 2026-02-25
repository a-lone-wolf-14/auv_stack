from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    return LaunchDescription([
        Node(package='auv_hardware',
             executable='vectornav_node'),

        Node(package='auv_hardware',
             executable='bar30_node'),

        Node(package='auv_hardware',
             executable='camera_front_node'),

        Node(package='auv_hardware',
             executable='camera_bottom_node'),

        Node(package='auv_hardware',
             executable='serial_thruster_driver'),
    ])