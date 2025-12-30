#!/bin/bash
# SPDX-FileCopyrightText: 2025 Yuto Matsushima
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bashrc

timeout 10 ros2 launch mypkg battery_check.launch.py > /tmp/mypkg.log

cat /tmp/mypkg.log |
grep 'Battery'
