import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import (IncludeLaunchDescription, GroupAction)
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration

import pdb
def generate_launch_description():
    # Path
    gazebo_launch_dir = os.path.join(get_package_share_directory('neuronbot2_gazebo'), 'launch')
    nb2nav_launch_dir = os.path.join(get_package_share_directory('neuronbot2_nav'), 'launch')
    nb2nav_map_dir = os.path.join(get_package_share_directory('neuronbot2_nav'), 'map')

    # Parameters
    use_sim_time = LaunchConfiguration('use_sim_time', default='True')
    open_rviz = LaunchConfiguration('open_rviz', default='True')
    ## mememan_world.model / phenix_world.model
    world_model = LaunchConfiguration('world_model', default='mememan_world.model')
    ## mememan.yaml / phenix.yaml
    map_path = LaunchConfiguration('map', default=nb2nav_map_dir+'/mememan.yaml')

    neuron_app_bringup = GroupAction([
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(os.path.join(gazebo_launch_dir, 'neuronbot2_world.launch.py')),
            launch_arguments={'use_sim_time': use_sim_time,
                              'world_model': world_model}.items()),

        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(os.path.join(nb2nav_launch_dir, 'bringup_launch.py')),
            launch_arguments={'use_sim_time': use_sim_time,
                              'open_rviz': open_rviz,
                              'map': map_path}.items()),
    ])

    ld = LaunchDescription()
    ld.add_action(neuron_app_bringup)
    return ld
