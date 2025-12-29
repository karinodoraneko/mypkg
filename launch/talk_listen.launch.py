import launch
import launch.actions
import launch.substitutions
import launch_ros.actions


def generate_launch_description():

    timer_pub = launch_ros.actions.Node(
        package='mypkg',
        executable='timer_pub',
        )
    time_sub = launch_ros.actions.Node(
        package='mypkg',
        executable='time_sub',
        output='screen'
        )

    return launch.LaunchDescription([timer_pub, time_sub])
