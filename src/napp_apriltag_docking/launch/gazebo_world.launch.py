import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import (IncludeLaunchDescription, GroupAction, DeclareLaunchArgument)
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PythonExpression
from launch.actions import ExecuteProcess
from launch.conditions import IfCondition
from launch_ros.actions import Node


import pdb
def generate_launch_description():
    # Path
    gazebo_launch_dir = os.path.join(get_package_share_directory('neuronbot2_gazebo'), 'launch')
    rviz_path = os.path.join(get_package_share_directory('napp_apriltag_docking'), 'rviz', 'default_tag.rviz')

    # Parameters
    use_sim_time = LaunchConfiguration('use_sim_time', default='True')
    world_model = LaunchConfiguration('world_model', default='tag.model')
    open_rviz = LaunchConfiguration('open_rviz', default='True')

    neuron_app_bringup = GroupAction([
        DeclareLaunchArgument(
            'open_rviz',
            default_value='true',
            description='Launch Rviz?'),

        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([gazebo_launch_dir, '/neuronbot2_world.launch.py']),
            launch_arguments={'use_sim_time': use_sim_time,
                              'use_camera': 'top',
                              'world_model': world_model}.items(),
        ),

        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            arguments=['-d', rviz_path],
            parameters=[{'use_sim_time': use_sim_time}],
            condition=IfCondition(LaunchConfiguration("open_rviz"))
            ),
        
    ])

    ld = LaunchDescription()
    ld.add_action(neuron_app_bringup)
    return ld
