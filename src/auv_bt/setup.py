from setuptools import setup, find_packages

package_name = 'auv_bt'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),

        ('share/' + package_name, ['package.xml']),

        ('share/' + package_name + '/launch', [
            'launch/bt.launch.py'
        ]),

        ('share/' + package_name + '/trees', [
            'trees/bt.xml'
        ]),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Suyash',
    maintainer_email='suyash14cs@gmail.com',
    description='AUV Behavior Tree Runner',
    license='Apache-2.0',

    entry_points={
        'console_scripts': [
            'bt_runner = auv_bt.bt:main'
        ],
    },
)
