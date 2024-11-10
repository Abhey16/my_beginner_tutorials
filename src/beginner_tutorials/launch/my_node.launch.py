from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    ld = LaunchDescription()

    my_pub_node = Node(
        package="beginner_tutorials",
        executable="my_node",
        # default value
        parameters=[
            {"publish_time":1}
        ]
    )

    ld.add_action(my_pub_node)

    return ld