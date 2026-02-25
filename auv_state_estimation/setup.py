from setuptools import setup
import os
from glob import glob

package_name = 'auv_state_estimation'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),

        ('share/' + package_name, ['package.xml']),

        # Install launch files
        (os.path.join('share', package_name, 'launch'),
            glob('launch/*.launch.py')),

        # Install config files
        (os.path.join('share', package_name, 'config'),
            glob('config/*.yaml')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='suyash',
    maintainer_email='suyash14cs@gmail.com',
    description='AUV state estimation (EKF)',
    license='Apache-2.0',
    entry_points={
        'console_scripts': [
            'ekf_node = auv_state_estimation.ekf_node:main',
        ],
    },
)