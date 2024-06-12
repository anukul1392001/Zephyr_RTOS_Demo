#include <zephyr/kernel.h>
#include <zephyr/sys/printk.h>
#include <stdlib.h>
#include <string.h>
#include <zephyr/random/random.h>
#include <zephyr/sys/ring_buffer.h>

#define STACK_SIZE 1024
#define THREAD1_PRIORITY 1
#define THREAD2_PRIORITY 2
#define BUFFER_SIZE 1024  

/**
 *  Globally accessible data structure 
 **/
struct ring_buf ring_buffer;
uint8_t ring_buffer_data[BUFFER_SIZE];

/** 
 * Mutex to protect access to the data buffer 
 * */
struct k_mutex buffer_mutex;

/** 
 * Thread function declarations 
*/
void thread1(void);
void thread2(void);

/** 
 * Thread stacks definations
 **/
K_THREAD_STACK_DEFINE(thread1_stack, STACK_SIZE);
K_THREAD_STACK_DEFINE(thread2_stack, STACK_SIZE);

/**
 * Thread data
 **/

struct k_thread thread1_data;
struct k_thread thread2_data;


/**
 * Thread 1: Generate Random Bytes and add to data buffer 
 **/
void thread1(void) {
    uint8_t rand_bytes[50];

    while (1) {
        k_mutex_lock(&buffer_mutex, K_FOREVER);

        uint8_t num_bytes = (sys_rand8_get() % 50) + 1;

        for (uint8_t i = 0; i < num_bytes; i++) {
            rand_bytes[i] = sys_rand8_get() % 256;
        }

        if (ring_buf_put(&ring_buffer, rand_bytes, num_bytes) == 0) {
            printk("Overflow!\n");
        }

        k_mutex_unlock(&buffer_mutex);

        k_sleep(K_SECONDS(1));
    }
}

/**
 * Thread 2: Print latest 512 bytes from data buffer and remove them 
 **/
void thread2(void) {
    uint8_t print_buffer[512];
    size_t buffer_len = 0;

    while (1) {
        k_sleep(K_SECONDS(10));

        k_mutex_lock(&buffer_mutex, K_FOREVER);

        if (ring_buf_size_get(&ring_buffer) >= 512) {

            buffer_len = ring_buf_get(&ring_buffer, print_buffer, 512);
            
            if (buffer_len == 512) {
                printk("Latest 512 bytes (in hex):\n");
                for (size_t i = 0; i < 512; i++) {
                    printk("%02x ", print_buffer[i]);
                }
                printk("\n");
            } else {
                printk("Error reading 512 Bytes\n");
            }
        }

        k_mutex_unlock(&buffer_mutex);
    }
}

void main(void) {

	/* Initialize Mutex, Ring Buffer & Create Threads. */
	
    k_mutex_init(&buffer_mutex);

    ring_buf_init(&ring_buffer, BUFFER_SIZE, ring_buffer_data);

    k_thread_create(&thread1_data, thread1_stack, STACK_SIZE,
                    (k_thread_entry_t)thread1, NULL, NULL, NULL,
                    THREAD1_PRIORITY, 0, K_NO_WAIT);

    k_thread_create(&thread2_data, thread2_stack, STACK_SIZE,
                    (k_thread_entry_t)thread2, NULL, NULL, NULL,
                    THREAD2_PRIORITY, 0, K_NO_WAIT);
}