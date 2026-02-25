from setuptools import setup
import os
from glob import glob

package_name = 'auv_hardware'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],  # this must match folder name
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'),
            glob('launch/*.launch.py')),
        (os.path.join('share', package_name, 'config'),
            glob('config/*.yaml')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Suyash',
    maintainer_email='you@example.com',
    description='AUV hardware interface',
    license='Apache License 2.0',
    entry_points={
        'console_scripts': [
            'vectornav_node = auv_hardware.vectornav_node:main',
            'bar30_node = auv_hardware.bar30_node:main',
            'serial_thruster_driver = auv_hardware.serial_thruster_driver:main',
            'camera_front_node = auv_hardware.camera_front_node:main',
            'camera_bottom_node = auv_hardware.camera_bottom_node:main',
        ],
    },
)