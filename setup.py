from setuptools import setup
import os
from glob import glob

package_name = 'ros2_timer'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*.launch.py'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Yuto Matsushima',
    maintainer_email='karinodoraneko@gmail.com',
    description='A simple timer package for ros2',
    license='BSD-3-Clause',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'timer_pub = ros2_timer.timer_pub:main',
            'time_sub = ros2_timer.time_sub:main',
        ],
    },
)
