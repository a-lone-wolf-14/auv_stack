from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():

    return LaunchDescription([

        Node(
            package='auv_bt',
            executable='bt_runner',
            output='screen'
        )

    ])
