# SPDX-FileCopyrightText: 2025 Yuto Matsushima
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

class Battery(Node):
    def __init__(self):
        super().__init__('battery')
        self.pub = self.create_publisher(Int16, 'battery_level', 10)
        self.create_timer(1.0, self.cb)
        self.level = 100

    def cb(self):
        msg = Int16()
        msg.data = self.level
        self.pub.publish(msg)
        self.get_logger().info(f'Battery: {self.level}%')
        
        if self.level > 0:
            self.level -= 1

def main():
    rclpy.init()
    node = Battery()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    rclpy.shutdown()
