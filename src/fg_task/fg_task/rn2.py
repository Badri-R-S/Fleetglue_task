#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer
from custom_msgs.action import Mission

class MissionActionServer(Node):
    def __init__(self):
        super().__init__('mission_server')
        self._action_server = ActionServer(
            self,
            Mission,
            'mission_action',
            execute_callback=self.execute_callback
        )

    async def execute_callback(self, goal_handle):
        #print("----------------------------RECEIVED_GOAL--------------------------------")
        self.get_logger().info(f'Received goal: {goal_handle.request}')
        goal_handle.succeed()

        result = Mission.Result()
        result.success = True
        result.message = 'Mission completed successfully'
        self.get_logger().info(f'Returning result: {result.message}')
        return result

def main(args=None):
    rclpy.init(args=args)
    mission_action_server = MissionActionServer()
    rclpy.spin(mission_action_server)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
