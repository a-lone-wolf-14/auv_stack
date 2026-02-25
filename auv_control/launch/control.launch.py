from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    return LaunchDescription([
        Node(package='auv_control',
             executable='control_node'),

        Node(package='auv_control',
             executable='thruster_mixer_node'),
    ])