from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(package="auv_hardware", executable="vectornav_node"),
        Node(package="auv_hardware", executable="bar30_node"),
        Node(package="auv_hardware", executable="serial_thruster_driver"),
        Node(package="auv_perception", executable="yolo_front_node"),
        Node(package="auv_state_estimation", executable="ekf_node"),
        Node(package="auv_control", executable="thruster_mixer_node"),
        Node(package="auv_mission", executable="mission_manager_node"),
    ])