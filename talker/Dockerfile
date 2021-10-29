FROM ros:foxy-ros-base as builder
WORKDIR /opt/ros/overlay_ws
RUN sed --in-place --expression '$isource "/opt/ros/overlay_ws/install/setup.bash"' /ros_entrypoint.sh

# install dependencies
COPY ./node/package.xml ./src/ros2/node/package.xml
RUN . /opt/ros/$ROS_DISTRO/setup.sh && \
    apt-get update && \
    rosdep install -y --from-paths src/ --ignore-src && \
    rm -rf /var/lib/apt/lists/*

# copy & build source
COPY ./node ./src/ros2/node
RUN . /opt/ros/$ROS_DISTRO/setup.sh && \
    colcon build --mixin release

FROM ros:foxy-ros-core as runtime
COPY --from=builder /opt/ros/overlay_ws/install /opt/ros/overlay_ws/install
COPY --from=builder /ros_entrypoint.sh /ros_entrypoint.sh
CMD [ "ros2", "run", "node", "talker" ]