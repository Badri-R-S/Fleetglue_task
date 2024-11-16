#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from custom_msgs.msg import Task # Imported custom message
import requests
import random

class TaskPublisher(Node):
    def __init__(self):
        super().__init__('task_publisher')
        # Sending task every 1 seconds
        self.timer = self.create_timer(1.0, self.send_task_to_api)

    def send_task_to_api(self):
        # Use custom message to create tasks
        msg = Task()
        msg.robot_id = random.randint(100,999)  # Random robot_id between 100 and 999
        msg.task = random.choice(["deliver_item", "pick_up_item", "inspect_area", "charge_battery"])
        msg.from_area = random.choice(["Warehouse A", "Warehouse B", "Charging Station", "Staging area"])
        msg.to_area = random.choice(["Warehouse A", "Warehouse B", "Charging Station", "Staging area"])
        msg.priority = random.choice(["low", "medium", "high"])

        # Convert to dictionary and then JSON format
        task_dict = {
            "robot_id": msg.robot_id,
            "task": msg.task,
            "from_area": msg.from_area,
            "to_area": msg.to_area,
            "priority": msg.priority
        }

        # Send the JSON to the web server via POST
        response = requests.post('http://localhost:5000/task', json=task_dict)
        #print("----------------------------POSTED_MISSION--------------------------------")
        #self.get_logger().info(f"Posted mission: {task_dict}")
        #self.get_logger().info(f"Response: {response.status_code}")

def main(args=None):
    rclpy.init(args=args)
    task_publisher = TaskPublisher()
    rclpy.spin(task_publisher)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
