# SPDX-FileCopyrightText: 2025 Yuto Matsushima
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

class Listener(Node):
    def __init__(self):
        super().__init__('listener')
        self.pub = self.create_subscription(Int16, 'battery_level', self.cb, 10)

    def cb(self, msg):
        if msg.data < 30:
            self.get_logger().warn(f'Low Battery! Level: {msg.data}%')
        else:
            self.get_logger().info(f'Battery Level: {msg.data}%')

def main():
    rclpy.init()
    node = Listener()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    rclpy.shutdown()
