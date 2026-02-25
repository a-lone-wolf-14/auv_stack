from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    return LaunchDescription([
        Node(package='auv_mission',
             executable='mission_manager_node',
             parameters=['config/mission.yaml']),
    ])