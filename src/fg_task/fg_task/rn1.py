#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from custom_msgs.action import Mission
import requests

class MissionClient(Node):
    def __init__(self):
        super().__init__('mission_client')
        self.action_client = ActionClient(self, Mission, 'mission_action')
        self.timer = self.create_timer(1.0, self.check_api_for_mission)

    def check_api_for_mission(self):
        response = requests.get('http://localhost:5000/task')
        if response.status_code == 200:
            mission_data = response.json()
            self.send_goal(mission_data)

    def send_goal(self, mission_data):
        goal_msg = Mission.Goal()
        goal_msg.robot_id = mission_data["robot_id"]
        goal_msg.task = mission_data["task"]
        goal_msg.from_area = mission_data["from_area"]
        goal_msg.to_area = mission_data["to_area"]
        goal_msg.priority = mission_data["priority"]

        #print("----------------------------SENDING_GOAL--------------------------------")
        #self.get_logger().info(f'Sending goal: {mission_data}')
        self.action_client.wait_for_server()
        self._send_goal_future = self.action_client.send_goal_async(
            goal_msg
            #feedback_callback=self.feedback_callback
        )
        self._send_goal_future.add_done_callback(self.goal_response_callback)

    def goal_response_callback(self, future):
        goal_handle = future.result()
        if not goal_handle.accepted:
            #self.get_logger().info('Goal rejected')
            return
        #self.get_logger().info('Goal accepted')
        self._get_result_future = goal_handle.get_result_async()
        #self._get_result_future.add_done_callback(self.get_result_callback)

    #def feedback_callback(self, feedback_msg):
        #self.get_logger().info(f'Feedback: {feedback_msg.feedback.status}')

    def get_result_callback(self, future):
        result = future.result().result
        #self.get_logger().info(f'Result: success={result.success}, message={result.message}')

def main(args=None):
    rclpy.init(args=args)
    mission_client = MissionClient()
    rclpy.spin(mission_client)
    rclpy.shutdown()

if __name__ == '__main__':
    main()