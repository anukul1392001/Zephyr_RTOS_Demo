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
    

# Psuedo Code

## Buffer Initialization
Initialize Ring Buffer
```pseudo
struct ring_buf ring_buffer;
```

## Thread 1: Buffer Writer

Thread 1 generates a random number of bytes and writes them to the buffer if there is enough space available.

```pseudo
Function thread1:
    Declare an array rand_bytes with size 50 to store random bytes

    Loop forever:
        Acquire the mutex lock on buffer_mutex

        Generate a random number between 1 and 50 and store it in num_bytes

        Loop from 0 to num_bytes-1:
            Generate a random byte and store it in rand_bytes at the current index

        If ring buffer cannot store all num_bytes from rand_bytes:
            Print "Overflow!"

        Release the mutex lock on buffer_mutex

        Sleep for 1 secondeep(k_seconds(1)); //Sleep for 1 sec
}
```

## Thread 2: Buffer Reader

Thread 2 checks if there are at least 512 bytes in the buffer. If so, it prints the latest 512 bytes and then removes them from the buffer.

```pseudo
Function thread2:
    Declare an array `print_buffer` of size 512
    Declare a variable `buffer_len` of type size_t, initialized to 0

    While true:
        Sleep for 10 seconds
        
        Acquire the mutex `buffer_mutex` with a timeout of forever

        If the size of `ring_buffer` is greater than or equal to 512:
            Retrieve 512 bytes from `ring_buffer` and store in `print_buffer`
            Set `buffer_len` to the number of bytes retrieved
            
            If `buffer_len` is equal to 512:
                Print "Latest 512 bytes (in hex):"
                For each byte in `print_buffer` from 0 to 511:
                    Print the byte in hexadecimal format
                Print a newline
            Else:
                Print "Error reading 512 Bytes"
        
        Release the mutex `buffer_mutex`

End Function
```

## Main Function

The `main` function initializes the mutex, ring buffer and creates the two threads.

```pseudo
int main() {
    Initialize Mutex
    Initialize Ring Buffer of Size BUFFER_SIZE = 1024
    Create thread1 with priority 1 and Stack Size STACK_SIZE = 1024 with no parameters passed
    Create thread1 with priority 2 and Stack Size STACK_SIZE = 1024 with no parameters passed

    return 0;
}
```
    
    
# References

    https://docs.zephyrproject.org/latest/kernel/data_structures/ring_buffers.html#implementation
    https://docs.zephyrproject.org/apidoc/latest/group__random__api.html#ga62cb24a6049b7aa9d03d66786e4a4db6
    https://docs.zephyrproject.org/latest/kernel/services/threads/index.html
