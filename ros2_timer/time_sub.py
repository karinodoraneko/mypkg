# SPDX-FileCopyrightText: 2025 Yuto Matsushima
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class TimeSubscriber(Node):
    def __init__(self):
        super().__init__('time_subscriber')
        self.sub = self.create_subscription(Int32, 'time_remaining', self.cb, 10)

    def cb(self, msg):
        if msg.data > 0:
            self.get_logger().info(f'Remaining: {msg.data} sec')
        else:
            self.get_logger().info('TIME UP!!')

def main():
    rclpy.init()
    node = TimeSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
