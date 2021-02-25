import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import (IncludeLaunchDescription, GroupAction, DeclareLaunchArgument)
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PythonExpression
from launch.actions import ExecuteProcess
from launch.conditions import IfCondition
from launch_ros.actions import Node


def generate_launch_description():

    docking_launch_dir = os.path.join(get_package_share_directory('apriltag_docking'), 'launch')

    neuron_app_bringup = GroupAction([
      
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([docking_launch_dir, '/autodock_gazebo.launch.py']),
        ),
    ])

    ld = LaunchDescription()
    ld.add_action(neuron_app_bringup)
    return ld
