from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():

    config = os.path.join(
        get_package_share_directory("auv_state_estimation"),
        "config",
        "ekf.yaml"
    )

    return LaunchDescription([
        Node(
            package='auv_state_estimation',
            executable='ekf_node',
            parameters=[config],
            output='screen'
        ),
    ])