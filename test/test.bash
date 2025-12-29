#!/bin/bash
# SPDX-FileCopyrightText: 2025 Yuto Matsushima
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source install/setup.bash

timeout 15 ros2 launch ros2_timer talk_listen.launch.py > /tmp/ros2_timer.log

cat /tmp/ros2_timer.log |
grep 'TIME UP!!'
