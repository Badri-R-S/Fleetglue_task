#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from custom_msgs.action import Task #Custom acton imported to store and send task to server
import requests

class TaskClient(Node):
    def __init__(self):
        super().__init__('task_client')
        #Defined Action client to send goal to server
        self.action_client = ActionClient(self, Task, 'task_action')
        #Timer created to send goal every second
        self.timer = self.create_timer(1.0, self.check_api_for_task)

    def check_api_for_task(self):
        #GET request made to the /task endpoint
        response = requests.get('http://localhost:5000/task')
        if response.status_code == 200:
            task_data = response.json()
            self.send_task(task_data)

    def send_task(self, task_data):
        #Task data received using custom action and prepared to be sent to server
        task_msg = Task.Goal()
        task_msg.robot_id = task_data["robot_id"]
        task_msg.task = task_data["task"]
        task_msg.from_area = task_data["from_area"]
        task_msg.to_area = task_data["to_area"]
        task_msg.priority = task_data["priority"]

        #print("----------------------------SENDING_GOAL--------------------------------")
        #self.get_logger().info(f'Sending goal: {mission_data}')
        self.action_client.wait_for_server()
        self._send_task_future = self.action_client.send_goal_async(
            task_msg
            #feedback_callback=self.feedback_callback
        )
        self._send_task_future.add_done_callback(self.task_response_callback)

    #Function that receives response from server and logs it
    def task_response_callback(self, future):
        task_handle = future.result()
        if not task_handle.accepted:
            #self.get_logger().info('Goal rejected')
            return
        #self.get_logger().info('Goal accepted')
        self._get_result_future = task_handle.get_result_async()
        #self._get_result_future.add_done_callback(self.get_result_callback)

    #def feedback_callback(self, feedback_msg):
        #self.get_logger().info(f'Feedback: {feedback_msg.feedback.status}')

    #def get_result_callback(self, future):
        #result = future.result().result
        #self.get_logger().info(f'Result: success={result.success}, message={result.message}')

def main(args=None):
    rclpy.init(args=args)
    task_client = TaskClient()
    rclpy.spin(task_client)
    rclpy.shutdown()

if __name__ == '__main__':
    main()