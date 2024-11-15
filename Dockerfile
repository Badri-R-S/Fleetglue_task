# Use ROS Humble base image
FROM ros:humble

# Update and install necessary dependencies
RUN apt-get update && apt-get install -y \
    ros-humble-rosidl-default-runtime \
    ros-humble-rosidl-default-generators \
    curl \
    python3-pip \
    python3-requests \
    && pip3 install flask \
    && rm -rf /var/lib/apt/lists/*

# Set up working directory
WORKDIR /ros_ws

# Copy your code
COPY ./src /ros_ws/src

# Build and source ROS workspace (use bash to source setup files)
RUN /bin/bash -c "source /opt/ros/humble/setup.bash && cd /ros_ws && colcon build && source install/setup.bash"

# Copy the entrypoint script and make it executable
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Set the entrypoint
ENTRYPOINT ["/entrypoint.sh"]

