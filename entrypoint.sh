#!/bin/bash

# Function to clean up background processes
cleanup() {
    echo "Cleaning up processes..."
    kill $FLASK_PID $TASK_PUBLISHER_PID $RN1_PID $RN2_PID
    wait $FLASK_PID $TASK_PUBLISHER_PID $RN1_PID $RN2_PID
    echo "Cleanup done."
}

# Trap SIGTERM and SIGINT to ensure cleanup
trap cleanup SIGTERM SIGINT

# Source the ROS 2 setup files
source /opt/ros/humble/setup.bash
source /ros_ws/install/setup.bash


python3 /ros_ws/src/fg_task/fg_task/app.py &
FLASK_PID=$!

sleep 5

# Run task_publisher in the background
ros2 run fg_task task_publisher &
TASK_PUBLISHER_PID=$!  # Get the process ID of task_publisher

# Wait a little to ensure task_publisher has started
sleep 2  # You can adjust the sleep time depending on your system

# Run rn1 in the background
ros2 run fg_task rn1 &
RN1_PID=$!  # Get the process ID of rn1

# Wait a little to ensure rn1 has started
sleep 2  # Adjust sleep as needed

# Run rn2 in the background
ros2 run fg_task rn2 &
RN2_PID=$!  # Get the process ID of rn2

# Wait for all processes to keep running
wait $FLASK_PID
wait $TASK_PUBLISHER_PID
wait $RN1_PID
wait $RN2_PID