#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from custom_msgs.msg import Mission # Import your custom message
import requests
import random

class MissionPublisher(Node):
    def __init__(self):
        super().__init__('mission_publisher')
        self.timer = self.create_timer(2.0, self.send_mission_to_api)

    def send_mission_to_api(self):
        # Create a custom mission message
        msg = Mission()
        msg.robot_id = random.randint(1, 1000)  # Random robot_id between 1 and 1000
        msg.task = random.choice(["deliver_package", "pick_up_item", "inspect_area", "charge_battery"])
        msg.from_area = random.choice(["Warehouse A", "Warehouse B", "Charging Station", "Docking Bay"])
        msg.to_area = random.choice(["Warehouse A", "Warehouse B", "Charging Station", "Docking Bay"])
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
    mission_publisher = MissionPublisher()
    rclpy.spin(mission_publisher)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
