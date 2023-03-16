# Base image
FROM ros:kinetic

# Install required packages
RUN apt-get update && \
    apt-get install -y ros-kinetic-rosbridge-suite ros-kinetic-web-video-server

# Copy ROS packages and launch files
COPY my_sensor_network /catkin_ws/src/
COPY my_launch_files /catkin_ws/src/

# Build ROS packages
RUN /bin/bash -c "source /opt/ros/kinetic/setup.bash && \
    cd /catkin_ws && \
    catkin_make"

# Expose ROS ports
EXPOSE 11311
EXPOSE 9090

# Set default command to launch ROS nodes
CMD ["roslaunch", "my_launch_files/my_sensor_network.launch"]
