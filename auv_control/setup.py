from setuptools import setup
import os
from glob import glob

package_name = 'auv_control'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
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
    maintainer='suyash',
    maintainer_email='suyash14cs@gmail.com',
    description='AUV control nodes',
    license='Apache-2.0',
    entry_points={
        'console_scripts': [
            'control_node = auv_control.control_node:main',
            'thruster_mixer_node = auv_control.thruster_mixer_node:main',
        ],
    },
)