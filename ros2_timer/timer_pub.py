# SPDX-FileCopyrightText: 2025 Yuto Matsushima
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class TimerPublisher(Node):
    def __init__(self):
        super().__init__('timer_publisher')
        self.pub = self.create_publisher(Int32, 'time_remaining', 10)
        self.create_timer(1.0, self.cb)
        self.count = 10

    def cb(self):
        msg = Int32()
        msg.data = self.count
        self.pub.publish(msg)
        
        if self.count > 0:
            self.count -= 1

def main():
    rclpy.init()
    node = TimerPublisher()
    rclpy.spin(node)
    
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
