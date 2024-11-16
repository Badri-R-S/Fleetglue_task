#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer
from custom_msgs.action import Task

class TaskServer(Node):
    def __init__(self):
        super().__init__('task_server')
        #Action server created to listen to client
        self._action_server = ActionServer(
            self,
            Task,
            'task_action',
            execute_callback=self.execute_callback
        )
        
    #Callback to send response to client after getting task
    async def execute_callback(self, task_handle):
        #print("----------------------------RECEIVED_GOAL--------------------------------")
        self.get_logger().info(f'Received Task: {task_handle.request}')
        task_handle.succeed()

        result = Task.Result()
        result.success = True
        result.message = 'Mission completed successfully'
        #self.get_logger().info(f'Returning result: {result.message}')
        return result

def main(args=None):
    rclpy.init(args=args)
    task_server = TaskServer()
    rclpy.spin(task_server)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
