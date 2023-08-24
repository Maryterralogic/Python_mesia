import threading
import time
import random

def produce(items, stop_event, max_items, produced_count):
    i = 1
    while not stop_event.is_set() and produced_count[0] < max_items:
        time.sleep(random.uniform(0, 2))
        items.append(i)
        with produced_count_lock:
            produced_count[0] += 1
        print("Produced:", i)
        i += 1

def consume(items, stop_event, max_items, consumed_count):
    while not stop_event.is_set() and consumed_count[0] < max_items:
        time.sleep(random.uniform(0, 2))
        if len(items) == 0:
            print("Consumed: No Items")
            continue
        item = items.pop(0)
        with consumed_count_lock:
            consumed_count[0] += 1
        print("Consumed:", item)

items = []
stop_flag = threading.Event()

num_producers = int(input("Enter the number of producers: "))
num_consumers = int(input("Enter the number of consumers: "))
max_items = int(input("Enter the maximum number of items: "))

producer_threads = []
consumer_threads = []
produced_count = [0]
consumed_count = [0]
produced_count_lock = threading.Lock()
consumed_count_lock = threading.Lock()

for _ in range(num_producers):
    thread = threading.Thread(target=produce, args=(items, stop_flag, max_items, produced_count))
    producer_threads.append(thread)
    thread.start()

for _ in range(num_consumers):
    thread = threading.Thread(target=consume, args=(items, stop_flag, max_items, consumed_count))
    consumer_threads.append(thread)
    thread.start()

try:
    for thread in producer_threads:
        thread.join()

    for thread in consumer_threads:
        thread.join()

    print("Both producers and consumers have finished.")
except KeyboardInterrupt:
    stop_flag.set()
    print("KeyboardInterrupt received. Stopping threads...")
