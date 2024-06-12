# Zephyr_RTOS_Demo
A small assignment project on Zephyr RTOS
____________________________________________________________________________________________________________________

# Setting Up Zephyr RTOS on Linux

This guide will help you set up Zephyr RTOS on Linux. Follow these steps to install all necessary tools and get started with your first Zephyr application.

## Prerequisites

Before starting, ensure you have the following installed on your Linux system:

- [Python 3.8 or later](https://www.python.org/downloads/)
- [CMake](https://cmake.org/download/)
- [west](https://docs.zephyrproject.org/latest/develop/west/index.html) (Zephyr's meta-tool)


Considering Prerequisites are already met we can proceed with the further steps.

Getting started guide:
    https://docs.zephyrproject.org/latest/develop/getting_started/index.html



## Step 1: Get Zephyr and install Python dependencies

  1. Create a new virtual environment:
    
    python3 -m venv ~/zephyrproject/.venv
  
  2. Activate the virtual environment:
  
    source ~/zephyrproject/.venv/bin/activate

Note :

Remember to activate the virtual environment every time you start working.

  3. Install west:
  
    pip install west

  4. Get the Zephyr source code:
    
    west init ~/zephyrproject
    cd ~/zephyrproject
    west update

  5. Export a Zephyr CMake package.
  
    west zephyr-export
  
  6. Zephyr’s scripts/requirements.txt file declares additional Python dependencies. Install     them with pip.
    
    pip install -r ~/zephyrproject/zephyr/scripts/requirements.txt


## Step 5: Install the Zephyr SDK

  1. Download and verify the Zephyr SDK bundle:
  
    cd ~
    wget https://github.com/zephyrproject-rtos/sdk-ng/releases/download/v0.16.8/zephyr-sdk-0.16.8_linux-x86_64.tar.xz
    wget -O - https://github.com/zephyrproject-rtos/sdk-ng/releases/download/v0.16.8/sha256.sum | shasum --check --ignore-missing


  2. Extract the Zephyr SDK bundle archive in $HOME location:

    tar xvf zephyr-sdk-0.16.8_linux-x86_64.tar.xz
    
  3. Run the Zephyr SDK bundle setup script:
  
    cd zephyr-sdk-0.16.8
    ./setup.sh

  4. Install udev rules, which allow you to flash most Zephyr boards as a regular user:

    sudo cp ~/zephyr-sdk-0.16.8/sysroots/x86_64-pokysdk-linux/usr/share/openocd/contrib/60-openocd.rules /etc/udev/rules.d
    sudo udevadm control --reload

# Running the Zephyr RTOS application

  1. Migrate to this directory:
  
    cd zephyrproject

  2. Activate the python virtual environment:

    source ~/zephyrproject/.venv/bin/activate
    
  3. Build the application program:
     My program lies in the directory ~/zephyrproject/demo

    west build -p always -b native_posix ~/zephyrproject/demo
    
  4. After successful build we should see output as mentioned  below:
    
    Generating files from /home/stark/zephyrproject/build/zephyr/zephyr.elf for 
    board: native_posix

  5. Run the program:

    ./build/zephyr/zephyr.exe
    
# References

    https://docs.zephyrproject.org/latest/kernel/data_structures/ring_buffers.html#implementation
    https://docs.zephyrproject.org/apidoc/latest/group__random__api.html#ga62cb24a6049b7aa9d03d66786e4a4db6
    https://docs.zephyrproject.org/latest/kernel/services/threads/index.html
