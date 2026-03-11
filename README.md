# Foundations of Robotic Assessment 1

### Setting Up the environment

Export the following to your shell's `.rc` file (most likely `.bashrc` or `.zshrc`)

```bash
# Example: Configuration for robot with domain ID 23 and discovery server at robot IP 192.168.1.201
export ROS_DOMAIN_ID=23
export ROS_HOSTNAME=192.168.1.201          # this laptop IP
export ROS_AUTOMATIC_DISCOVERY_RANGE=SUBNET # only discover nodes on the same subnet
export RMW_IMPLEMENTATION=rmw_fastrtps_cpp # ensure Fast DDS is used
export ROS_DISCOVERY_SERVER=192.168.1.101:11811  # discovery server location (robot IP:port)
export ROS_SUPER_CLIENT=True                # enable super client mode (optional)
```
